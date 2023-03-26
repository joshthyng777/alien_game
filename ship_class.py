import pygame
from settings import Settings

class Ship():
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        #Add ship image
        self.image = pygame.image.load('spaceshipComp.png')
        self.rect = self.image.get_rect()
        
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right: #Makes sure it cant leave screen
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0: #Makes sure left side cant leave screen
            self.x -= self.settings.ship_speed
            
        self.rect.x = self.x
        
    def blitme(self):
        self.screen.blit(self.image, self.rect) #Creats the ship at location