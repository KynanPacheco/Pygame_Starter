import pygame
import Game.Manager as Manager

class PlayGame(pygame.sprite.Sprite):
    def __init__(self):
        super(PlayGame, self).__init__()
        self.surf = Manager.FONT.render('Play Game', False, (173, 173, 173))
        self.rect = self.surf.get_rect()

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.surf = Manager.FONT.render('Play Game', False, (255, 255, 255))
        else:
            self.surf = Manager.FONT.render('Play Game', False, (173, 173, 173))
    
    def clicked(self):
        Manager.ChangeScene("Game")

class Settings(pygame.sprite.Sprite):
    def __init__(self):
        super(Settings, self).__init__()
        self.surf = Manager.FONT.render('Settings', False, (173, 173, 173))
        self.rect = self.surf.get_rect()

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.surf = Manager.FONT.render('Settings', False, (255, 255, 255))
        else:
            self.surf = Manager.FONT.render('Settings', False, (173, 173, 173))

    def clicked(self):
        Manager.ChangeScene("Settings")