import pygame

from pygame.locals import RLEACCEL
from constants import *

class Fighter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #self.surf = pygame.Surface((100, 100))
        self.surf = pygame.image.load("assets/player.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.midtop = mouse_pos[0], SCREEN_HEIGHT - self.rect.height