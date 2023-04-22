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
        self.surf = pygame.image.load(ENEMY.png).convert()

        # Remove the black background
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)

        # Sets pumpkin to middle of the screen
        self.rect = self.surf.get_rect(center = (800, BACKGROUND_HEIGHT / 2))


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


