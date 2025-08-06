import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.setting
        self.moving_right = False
        self.moving_left = False
        self.screen_rect = self.screen.get_rect()
        
        # Load the ship image and resize it while maintaining aspect ratio
        self.image = pygame.image.load('ship2.bmp')
        self.original_rect = self.image.get_rect()
        self.aspect_ratio = self.original_rect.height / self.original_rect.width
        self.new_width = 150  # Adjust the new width as needed
        self.new_height = int(self.new_width * self.aspect_ratio)
        self.image = pygame.transform.scale(self.image, (self.new_width, self.new_height))
        
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
