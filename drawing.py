import pygame
from settings import *
from ray_casting import ray_casting
from map import mini_map


class Drawing:
    def __init__(self, sc, mini_map):
        self.sc = sc
        self.mini_map = mini_map
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.textures = {
            '1': pygame.image.load('img/texture1.bmp').convert(),
            '2': pygame.image.load('img/texture2.jpg').convert(),
            '3': pygame.image.load('img/first.jpg').convert(),
            '4': pygame.image.load('img/first.jpg').convert()
        }

    def background(self):
        pygame.draw.rect(self.sc, SKY, (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(self.sc, ASPHALT, (0, HALF_HEIGHT, WIDTH, HEIGHT))

    def world(self, player_pos, player_angle):
        ray_casting(self.sc, player_pos, player_angle, self.textures)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, False, RED)
        self.sc.blit(render, FPS_POSITION)

    def minimap(self, player):
        self.mini_map.fill(BLACK)
        x, y = player.x // MAP_SCALE, player.y // MAP_SCALE

        pygame.draw.circle(self.mini_map, GREEN, (int(x), int(y)), 3)
        pygame.draw.line(self.mini_map, BLUE , (x, y), (x + WIDTH // (MAP_SCALE * 2) * math.cos(player.angle),
                                                y + WIDTH // (MAP_SCALE * 2) * math.sin(player.angle)))
        for x, y in mini_map:
            pygame.draw.rect(self.mini_map, WHITE, (x, y, TILE_SCALE, TILE_SCALE), 2)
        self.mini_map.set_colorkey(BLACK)
        self.sc.blit(self.mini_map, (0, 0))

    def speedometer(self, player):
        render = self.font.render(str(int(player.speed)), False, RED)
        self.sc.blit(render, SPEEDOMETER_POSITION)

    def tachometer(self, player):
        render = self.font.render(str(int(player.rpm)), False, RED)
        self.sc.blit(render, TACHOMETER_POSITION)

    def transmission(self, player):
        render = self.font.render(str(int(player.mode) - 1), False, RED)
        self.sc.blit(render, TRANSMISSION_POSITION)