import pygame
from sprite_sheet import SpriteSheet

class Explosion(pygame.sprite.Sprite):
    def __init__(self, rect):
        super().__init__()
        explosion_sheet = SpriteSheet(filename="assets/explode3.bmp")
        self.animation = []
        self.animation.append(pygame.transform.scale(explosion_sheet.get_image(0, 0, 48, 48), (98, 98)))
        self.animation.append(pygame.transform.scale(explosion_sheet.get_image(48, 0, 48, 48), (98, 98)))
        self.animation.append(pygame.transform.scale(explosion_sheet.get_image(96, 0, 48, 48), (98, 98)))
        self.animation.append(pygame.transform.scale(explosion_sheet.get_image(144, 0, 48, 48), (98, 98)))
        self.animation.append(pygame.transform.scale(explosion_sheet.get_image(0, 48, 48, 48), (98, 98)))
        self.animation.append(pygame.transform.scale(explosion_sheet.get_image(48, 48, 48, 48), (98, 98)))
        self.animation.append(pygame.transform.scale(explosion_sheet.get_image(96, 48, 48, 48), (98, 98)))
        self.animation.append(pygame.transform.scale(explosion_sheet.get_image(144, 48, 48, 48), (1920, 1080)))
        
        self.parent_rect = rect
        self.surf = self.animation[0]
        self.rect = self.surf.get_rect(
            center=(self.parent_rect.centerx, self.parent_rect.centery)
        )
        self.animations = iter(self.animation)
        
    def update(self):
        try:
            self.surf = next(self.animations)
            self.rect = self.surf.get_rect(
                center=(self.parent_rect.centerx, self.parent_rect.centery)
            )
            print('Anthony')
        except StopIteration:
            self.kill()
    