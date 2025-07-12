import pygame
import Game.Manager as Manager
from pygame.locals import *


def Init_Scene():
    pass

def Loop():
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                Manager.running = False
            if event.key == QUIT:
                Manager.running = False
        
        if event.type == Manager.Game_Tick:
            pass
