from settings import *
from map import world_map, texture_world_map
import pygame


def mapping(a, b):  # Координаты верхнего угла квадрата, где находятся a и b
    return (a // TILE) * TILE, (b // TILE) * TILE


power = []
def precalc_power():
    global power
    power = [1]
    for i in range(10000):
        power.append(power[-1] * 1.0011551)


def ray_casting(sc, player_pos, player_angle, textures):
    ox, oy = player_pos  # Координаты игрока
    xm, ym = mapping(ox, oy)  # Координаты клетки игрока
    chx, chy, cvx, cvy, cx, cy = 0, 0, 0, 0, 0, 0
    colors1 = ()
    colors2 = ()
    color = ()
    cur_angle = player_angle - HALF_FOV
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        # verticals
        if cos_a >= 0:
            x = xm + TILE
            dx = 1
        else:
            x = xm
            dx = -1
        for i in range(0, 4 * WIDTH, TILE):
            depth_v = (x - ox) / cos_a
            yv = oy + depth_v * sin_a
            if mapping(x + dx, yv) in world_map:
                cx = x
                colors1 = mapping(x + dx, yv)
                break
            x += dx * TILE

        # horizontals
        if sin_a >= 0:
            y = ym + TILE
            dy = 1
        else:
            y = ym
            dy = -1
        for i in range(0, 4 * HEIGHT, TILE):
            depth_h = (y - oy) / sin_a
            xh = ox + depth_h * cos_a
            if mapping(xh, y + dy) in world_map:
                colors2 = mapping(xh, y + dy)
                cy = y
                break
            y += dy * TILE

        # projection

        if depth_v <= depth_h:
            depth = depth_v       # problem # починил гыгы
            offset = int(yv) % TILE
            color = colors1
        else:
            offset = int(xh) % TILE
            depth = depth_h
            color = colors2

        if len(colors1) == 0 or len(colors2) == 0:
            crash = [colors1, colors2]
            crash.sort(key=len, reverse=True)
            color = crash[0]
            if len(color) == 0:
                color = (0, 0)
        color_flag = texture_world_map[color]

        depth = max(depth, 0.00000000001)
        depth *= math.cos(cur_angle - player_angle)
        proj_height = min(int(PROJ_COEFF / depth), 2 * HEIGHT)
        texture = textures[str(color_flag)]

        wall_column = texture.subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)
        wall_column = pygame.transform.scale(wall_column, (int(SCALE), int(proj_height)))
        sc.blit(wall_column, (ray * SCALE, HALF_HEIGHT - proj_height // 2))
        srf = pygame.Surface((int(SCALE), int(proj_height)))
        srf.fill(SKY)
        srf.set_alpha(min(255, int(power[int(depth)])))
        sc.blit(srf, (ray * SCALE, HALF_HEIGHT - proj_height // 2))


        cur_angle += DELTA_ANGLE
