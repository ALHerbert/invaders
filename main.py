import pygame

from pygame.locals import (
    FULLSCREEN,
    KEYDOWN,
    K_ESCAPE,
    K_SPACE,
    QUIT,
    MOUSEBUTTONDOWN,
    RLEACCEL
)
from constants import *

# game objects
from bullet import Bullet
from invader import Invader
from fighter import Fighter
from explosion import Explosion

# init and set up display
pygame.mixer.init()
pygame.init()

modes = pygame.display.list_modes(32)
screen = pygame.display.set_mode((0,0), 32)
pygame.mouse.set_visible(0)

def main():
    # create sprite groups
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    invaders = pygame.sprite.Group()
    explosions = pygame.sprite.Group()

    fighter = Fighter()
    all_sprites.add(fighter)

    # load assets
    bg = pygame.image.load("assets/starBackground.png")
    fire_laser = pygame.mixer.Sound("assets/laser7.wav")
    explosion = pygame.mixer.Sound("assets/DeathFlash.wav")

    

    # add text
    bg = pygame.transform.scale(bg, (1920, 1080))
    font = pygame.font.Font(None, 72)

    # game variables
    score = 0
    current_speed = 5

    # main loop
    clock = pygame.time.Clock()
    pygame.time.set_timer(ADD_INVADER, 1000)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                fire_laser.play()
                new_bullet = Bullet()
                bullets.add(new_bullet)
                all_sprites.add(new_bullet)
            elif event.type == ADD_INVADER:
                new_invader = Invader(current_speed)
                invaders.add(new_invader)
                all_sprites.add(new_invader)
                current_speed += 1

        fighter.update()
        bullets.update()
        invaders.update()
        explosions.update()

        if pygame.sprite.spritecollideany(fighter, invaders):
            fighter.kill()
            running = False

        for entity in pygame.sprite.groupcollide(invaders, bullets, 1, 1):
            score += 1
            explosion.play()
            new_explosion = Explosion(entity.rect)
            all_sprites.add(new_explosion)
            explosions.add(new_explosion)

        screen.fill((255,255,255))
        screen.blit(bg, (0,0))
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        text = font.render(f"Score: {score}", 1, (250, 250, 250))
        textpos = 0, 0

        screen.blit(text, textpos)
        pygame.display.flip()

        clock.tick(30)

    menu()

# menu
def menu():
    font = pygame.font.Font(None, 125)

    menu_running = True
    while menu_running:
        # get events
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    menu_running = False
                    pygame.quit()
                elif event.key == K_SPACE:
                    menu_running = False
                    main()
            elif event.type == QUIT:
                    menu_running = False
                    pygame.quit()
                
        # update
        # draw
        screen.fill((255,255,255))
        text = font.render("Please spacebar to play. Press ESC to quit.", 1, (0, 0, 0))
        textpos = 50, SCREEN_HEIGHT / 2

        screen.blit(text, textpos)

        pygame.display.flip()

menu()