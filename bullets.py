import pygame
from setting import Setting
from pygame.sprite import Sprite
class Bullet(Sprite):
    # class made for manage bullet
    def __init__(self,ai_game):
        super().__init__()
        # craete a bullete at ships current position
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.colour = self.setting.bullet_colour
        # create bullete rect at (o,o) and then set correct position
        self.rect = pygame.Rect(0,0,self.setting.bullet_width,self.setting.bullet_hieght)
        self.rect.midtop = ai_game.ship.rect.midtop
        # store the bullete position in float
        self.y = float(self.rect.y)
    def update(self):
        # move the bullete upward on the screen
        self.y-=self.setting.bullet_speed
        # update the rect position
        self.rect.y = self.y
    def draw_bullet(self):
        # draw bullet on the screen
        pygame.draw.rect(self.screen,self.colour,self.rect)