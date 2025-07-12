import pygame
import Game.Manager as Manager
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.surface.Surface((50, 50))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    def update(self):
        pass
