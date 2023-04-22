
import pygame
from pygame.locals import K_DOWN, K_LEFT, K_RIGHT, K_UP, RLEACCEL 

from constants import *

class Hero(pygame.sprite.Sprite):

    lives: int = 3

    def __init__(self) -> None:
        super(Hero, self).__init__()

        self.surf = pygame.image.load(HERO).convert()
        
        self.speed = HERO_SPEED

        self.rect = self.surf.get_rect(center = (50, SCREEN_HEIGHT / 2))
    
