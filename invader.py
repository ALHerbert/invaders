import pygame
import random

from pygame.locals import RLEACCEL
from constants import *

class Invader(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.surf = pygame.image.load("assets/enemyShip.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0, SCREEN_WIDTH),
                random.randint(-100, -20)
            )
        )
        self.speed = speed

    def update(self):
        self.rect.move_ip(0, self.speed)