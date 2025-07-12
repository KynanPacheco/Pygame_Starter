import pygame
import Game.Scenes as Scenes
import os
import importlib

# Centralized Game Manager available to other modules for settings, game state, and scene managment

# Initialize Pygame
pygame.init()

# Calculate Screen Resolution
desktop = pygame.display.get_desktop_sizes()
SCREEN_WIDTH = desktop[0][0]
SCREEN_HEIGHT = desktop[0][1]

# Set Game Clock Speed
FPS = 30
clock = pygame.time.Clock()

# Game Settings
BACKGROUND = (0, 0, 0)
FONT = pygame.font.SysFont('Fixedsys Regular', 30)
SCENE = "Debug"
running = True
STATE = "init"

# Custom Event Types
Game_Tick = pygame.event.custom_type()

# Initialize Sprite Groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
ui = pygame.sprite.Group()

# Initialize Display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)

# Scene Management Functions
def LoadScene(scene):
    for file in os.listdir(os.path.join(os.path.dirname(__file__), 'Scenes')):
        if file.endswith(".py") and file.strip(".py") == scene:
            scene = importlib.import_module("Game.Scenes." + file.strip(".py"))
            scene.Loop()

def ChangeScene(scene):
    SCENE = scene
    for file in os.listdir(os.path.join(os.path.dirname(__file__), 'Scenes')):
        if file.endswith(".py") and file.strip(".py") == scene:
            scene = importlib.import_module("Game.Scenes." + file.strip(".py"))
            scene.Init_Scene()