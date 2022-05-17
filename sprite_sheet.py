import pygame
from constants import *
from pygame.locals import (
    RLEACCEL
)

class SpriteSheet:
    def __init__(self, filename):
        self.sprite_sheet = pygame.image.load(filename).convert()
        

    def get_image(self, posx, posy, width, height):
        image = pygame.Surface([width, height]).convert()
        image.blit(self.sprite_sheet, (0, 0), (posx, posy, width, height))
        image.set_colorkey((69, 78, 91), RLEACCEL)

        return image