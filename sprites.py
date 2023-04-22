
import pygame
from pygame.locals import K_DOWN, K_LEFT, K_RIGHT, K_UP, RLEACCEL 

from constants import *

class Hero(pygame.sprite.Sprite):

    lives: int = 3
    gravity: int = 10 

    def __init__(self) -> None:
        super(Hero, self).__init__()

        self.surf = pygame.image.load(HERO).convert()
        self.gravity = 1
        
        self.speed = HERO_SPEED

        self.rect = self.surf.get_rect(center = (50, 350))
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)

    def update(self, pressed_keys) -> None:
        
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if random.randint(1, 5) == 5: 
            self.rect.move_ip(0, self.gravity)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 875:
            self.rect.right = 875
        if self.rect.top <= 50:
            self.rect.top = 50
        if self.rect.bottom >= 500:
            self.rect.bottom = 500
    
    def jump(self):
        self.rect.move_ip(0, -250)


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
        self.rect = self.surf.get_rect(center = (750, 250))



class Projectile(pygame.sprite.Sprite):
    """Projectiles aka bullets aka."""

    def __init__(self) -> None:
        # Super class initialization of the sprite
        super(Projectile, self).__init__()

        

        # Create the image for the enemy to be, convert it
        image_path = BULLET
        self.surf = pygame.image.load(image_path).convert()
        self.surf = pygame.transform.scale(self.surf, (60, 60))

        # Remove the black background
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)

        # Spawns the bullets from the pumpkin
        self.rect = self.surf.get_rect(center = (620, BACKGROUND_HEIGHT / 2))

        # Set their speed to the constant from the constants file
        self.speed = BULLET_SPEED

    def update(self):
        self.rect.move_ip(-self.speed, 0)

            
    
