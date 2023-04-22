import pygame
from pygame.locals import K_DOWN, K_LEFT, K_RIGHT, K_UP, RLEACCEL

class Enemy(pygame.sprite.Sprite):
    """Evil pumpkin."""

    def __init__(self) -> None:
        # Super class initialization of the sprite
        super(Enemy, self).__init__()
        
        # Create the image for the enemy to be, convert it
        self.surf = pygame.image.load(enemy.png).convert()

        # Remove the black background
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)

class Projectile(object):
    """Bullets."""

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.surf = pygame.image.load(enemy.png).convert()

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
