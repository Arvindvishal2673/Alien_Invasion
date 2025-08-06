import pygame
from pygame.sprite import Sprite
class Alien (Sprite):
    # A class that represent alien in game 
    def __init__(self,ai_game):
        # initialise th ealien and set it initial position
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.image = pygame.image.load('alien3.bmp')
        self.original_rect = self.image.get_rect()
        self.aspect_ratio = self.original_rect.height / self.original_rect.width
        self.new_width = 90 # Adjust the new width as needed
        self.new_height = int(self.new_width * self.aspect_ratio)
        self.image = pygame.transform.scale(self.image, (self.new_width, self.new_height))
        self.rect = self.image.get_rect()
        # start each new alien from top left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # store alien exactly horizontal possition
        self.x = float(self.rect.x)
    def  check_edge(self):
        # check either alien fleet touch the edge
        screen_rect = self.screen.get_rect()
        if self.rect.right>= screen_rect.right:
            self.setting.fleet_direction = -1
        if self.rect.left <= 0:
            self.setting.fleet_direction = 1
    def update_alien(self):
        if self.setting.fleet_direction == 1:
            self.rect.x+=self.setting.alien_speed
            self.rect.y+=self.setting.fleet_drop_speed
        elif self.setting.fleet_direction == -1:
            self.rect.x-=self.setting.alien_speed
            self.rect.y+=self.setting.fleet_drop_speed
    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)



   
