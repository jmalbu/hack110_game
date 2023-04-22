
import pygame
from pygame.locals import K_DOWN, K_LEFT, K_RIGHT, K_UP, RLEACCEL 

from constants import *

class Hero(pygame.sprite.Sprite):

    lives: int = 3

    def __init__(self) -> None:
        super(Hero, self).__init__()

        self.surf = pygame.image.load(HERO).convert()
        
        self.speed = HERO_SPEED

        self.rect = self.surf.get_rect(center = (50, 350))
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

from constants import *
import pygame
from pygame.locals import RLEACCEL
import random

class Enemy(pygame.sprite.Sprite):
    """Evil pumpkin."""

    def __init__(self) -> None:
        # Super class initialization of the sprite
        super(Enemy, self).__init__()
        
        # Create the image for the enemy to be, convert it
        self.surf = pygame.image.load(ENEMY).convert()

        # Remove the black background
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)

        # Sets pumpkin to middle of the screen
        self.rect = self.surf.get_rect(center = (750, 300))



class Projectile(pygame.sprite.Sprite):
    """Projectiles aka bullets aka."""

    def __init__(self) -> None:
        # Super class initialization of the sprite
        super(Enemy, self).__init__()

        # Create the image for the enemy to be, convert it
        image_path = BULLET
        self.surf = pygame.image.load(image_path).convert()

        # Remove the black background
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)

        # Spawns the bullets from the pumpkin
        self.rect = self.surf.get_rect(center = (800, BACKGROUND_HEIGHT / 2))

        # Set their speed to the constant from the constants file
        self.speed = BULLET_SPEED

            
    
