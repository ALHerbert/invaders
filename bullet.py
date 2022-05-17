import pygame

from pygame.locals import RLEACCEL
from constants import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load("assets/laserGreen.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                pygame.mouse.get_pos()[0],
                SCREEN_HEIGHT - 10
            )
        )

    def update(self):
        self.rect.move_ip(0, -50)