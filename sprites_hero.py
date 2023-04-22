
import pygame
from pygame.locals import K_DOWN, K_LEFT, K_RIGHT, K_UP, RLEACCEL 

from constants import *

class Hero(pygame.sprite.Sprite):

    lives: int = 3

    def __init__(self) -> None:
        super(Hero, self).__init__()

        self.surf = pygame.image.load(HERO).convert()
        
        self.speed = HERO_SPEED

        self.rect = self.surf.get_rect(center = (70, SCREEN_HEIGHT / 2))
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)

    def update(self, pressed_keys) -> None:
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 50:
            self.rect.top = 50
        if self.rect.bottom >= 550:
            self.rect.bottom = 550
            
    
