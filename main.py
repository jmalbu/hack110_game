import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

from background import *
from constants import *
from sprites import *

pygame.init()

SHOOT_BULLETS = pygame.USEREVENT
pygame.time.set_timer(SHOOT_BULLETS, TIMED_BULLET, NUM_BULLET)

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
background = Background()
enemy = Enemy()
hero = Hero()
projectile = Projectile()
all_projectiles = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(enemy)
all_sprites.add(hero)
all_sprites.add(projectile)
all_projectiles.add(projectile)


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_UP: 
                    hero.jump()
            elif event.type == SHOOT_BULLETS:
                new_bullet = Projectile()
                all_sprites.add(new_bullet)
                all_projectiles.add(new_bullet)
                    
        background.render(screen)

        for sprite in all_sprites: 
            screen.blit(sprite.surf, sprite.rect)
        pygame.display.flip()
        
        pressed_keys = pygame.key.get_pressed()
        hero.update(pressed_keys)
        enemy.update(hero, enemy)

        for projectile in all_projectiles: 
            projectile.update()

        
        

#Hero.update(pressed_keys)

if __name__ == '__main__':
    main()

