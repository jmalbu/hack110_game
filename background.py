import pygame
from constants import *

class Background():

    def __init__(self):
        super(Background, self).__init__()

        surface = pygame.image.load(BACKGROUND).convert()

        self.surf = pygame.transform.scale(surface, (BACKGROUND_WIDTH, BACKGROUND_HEIGHT))
        self.x = 0
        self.y = 0

    
    def render(self, screen):
        screen.blit(self.surf, (self.x, self.y))

