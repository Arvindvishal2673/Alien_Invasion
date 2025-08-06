import pygame
import pygame.font
class Buttom:
    # A class to build buttom for game 
    def prep_msg(self,msg):
        # method to render message into image
        self.msg_image = self.font.render(msg, True, self.text_colour, self.buttom_colour)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.screen_rect.center
        
    def draw_buttom(self):
        # a method to show buttom on screen
        self.screen.fill(self.buttom_colour,self.buttom_rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        pygame.draw.circle(self.screen,self.circle_colour,self.circle_center,self.circle_radius)
        pygame.draw.circle(self.screen,self.circle_colour,(875,450),self.circle_radius)
    def __init__(self,ai_game,msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        # set properties of circlr to make rectangular look curved edge
        self.circle_center = (575,450)
        self.circle_colour = (0,135,0)
        self.circle_radius = 35
        # set dimension and properties of buttom
        self.width,self.height = 300,70
        self.buttom_colour = (0,135,0)
        self.text_colour = (255,255,255)
        self.font = pygame.font.SysFont(None,48)
        # build buttom's rect object and centre it
        self.buttom_rect = pygame.Rect(0,0,self.width,self.height)
        self.buttom_rect.center = self.screen_rect.center
        self.prep_msg(msg)

