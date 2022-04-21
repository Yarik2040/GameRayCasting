from settings import *
from map import world_map
from speeding import speeding, reverse_speeding, stopping
import pygame
import math


class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle
        self.rpm = 0
        self.mode = 1
        self.speed = 0.0
        self.fps = 46

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        keys = pygame.key.get_pressed()
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        self.old_cords = []
        if len(self.old_cords) < 5:
            self.old_cords.append((self.x, self.y))
        else:
            self.old_cords = self.old_cords[1:]
            self.old_cords.append((self.x, self.y))
        old_x = self.x
        old_y = self.y
        if keys[pygame.K_w]:
            self.rpm += 100 * RPM_FACTOR[self.mode]
            if self.mode != 0:
                if self.speed < SPEED_DATA[self.mode] + 2:
                    self.speed += speeding(self.speed, self.mode, self.rpm)
                else:
                    self.speed += stopping(self.speed)
            else:
                if abs(self.speed) < abs(SPEED_DATA[self.mode]) + 20:
                    buff = reverse_speeding(self.speed, self.rpm)
                    self.speed = max(self.speed - buff, SPEED_DATA[0])
                else:
                    self.speed -= stopping(self.speed)
        else:
            self.rpm -= 100
            self.speed += stopping(self.speed)
            self.speed = max(0, self.speed)
        self.rpm = min(7000, max(0, self.rpm))

        player_speed = self.speed

        self.x += player_speed * cos_a
        self.y += player_speed * sin_a

        if keys[pygame.K_s]:
            self.speed += stopping(self.speed) * 2
        if keys[pygame.K_a] and int(self.speed) != 0:
            self.angle -= 0.02
        if keys[pygame.K_d] and int(self.speed) != 0:
            self.angle += 0.02

        if keys[pygame.K_e]:
            if self.fps > 20:
                if self.mode < 6:
                    self.rpm = max(0, self.rpm - 2500)
                    self.mode += 1
                    self.fps = 0

        if keys[pygame.K_q]:
            if self.fps > 20:
                if self.mode > 0:
                    if self.rpm > 0:
                        self.rpm = min(7000, self.rpm + 2500)
                    else:
                        self.rpm = min(7000, self.rpm)
                    self.mode -= 1
                    self.fps = 0

        self.fps += 1
        new_x = self.x // TILE * TILE
        new_y = self.y // TILE * TILE

        if (new_x, old_y // TILE * TILE) in world_map:
            self.x = self.old_cords[0][0]

        if (old_x // TILE * TILE, new_y) in world_map:
            self.y = self.old_cords[0][1]

