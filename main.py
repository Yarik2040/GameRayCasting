from settings import *
from map import *
from drawing import Drawing
from player import Player
import pygame
import ray_casting

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
minimap = pygame.Surface((WIDTH // MAP_SCALE * MAPPING_SCALE, HEIGHT // MAP_SCALE * MAPPING_SCALE))  # !!!
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc, minimap)
ray_casting.precalc_power()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.movement()
    sc.fill(BLACK)

    drawing.background()
    drawing.world(player.pos, player.angle)

    drawing.minimap(player)
    fps = drawing.fps(clock)
    drawing.speedometer(player)
    drawing.tachometer(player)
    drawing.transmission(player)

    pygame.display.flip()
    clock.tick(50)
