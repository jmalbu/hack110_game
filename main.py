import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

from background import *
from constants import *
from sprites_hero import *

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
background = Background()
hero = Hero()
enemy = Enemy()
all_sprites = pygame.sprite.Group()
all_sprites.add(hero)
all_sprites.add(enemy)

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        background.render(screen)

        for sprite in all_sprites: 
            screen.blit(sprite.surf, sprite.rect)
        pygame.display.flip()
        
        pressed_keys = pygame.key.get_pressed()
        hero.update(pressed_keys)
        
        

#Hero.update(pressed_keys)

if __name__ == '__main__':
    main()

