import pygame
from constants import *

class Background():

    def __init__(self):
        super(Background, self).__init__()

        surface = pygame.image.load(BACKGROUND)
        