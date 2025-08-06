import sys
from ship import Ship
from time import sleep
from game_states import Game_stats
import pygame
from setting import Setting
from bullets import Bullet
from alien import Alien
from random import randint
from buttom import Buttom
from scoreboard import SCORING_SYSTEM
pygame.init()
pygame.mixer.init()
import warnings

# Suppress libpng warnings
warnings.filterwarnings("ignore", category=Warning, module="libpng")

class GAME_ENVIRONMENT:
    '''A class to manage element,resource of game(alien invasion)'''
    def check_play_buttom(self,pos):
        # start new game when click play buttom
        self.buttom_clicked = self.play_buttom.buttom_rect.collidepoint(pos)
        # check click for buttom and activity of game
        if self.buttom_clicked and not self.game_active:
            # reset the stats of game
            self.stats.reset_stats()
            self.sb.prep_ships()
            self.sb.prep_score()
            self.playing_sound.play()
            self.game_active = True
            # clear last states
            self.bullete.empty()
            self.aliens.empty()
            # create new states for new game
            self.creat_fleet()
            self.ship.center_ship()
    def ship_hit(self):
        """Respond to the ship being hit by an alien.""" 
        # decreament ship left
        self.setting.limit-=1
        # get rid of remaining bullets and aliens
        self.bullete.empty()
        self.aliens.empty()
        if self.setting.limit >0:
            # Decrement ships_left, and update scoreboard.
            self.sb.prep_ships()
            # create new fleets and centre the ship
            self.creat_fleet() 
            self.ship.center_ship()
            # pause
            sleep(0.5)
        else :
            self.game_active = False
            pygame.mouse.set_visible(True)
    def check_alien_buttom(self):
        # check wheather alien hit the buttom of screen
        for alien in self.aliens.sprites():
            if alien.rect.buttom >= self.setting.screen_hieght:
                self.ship_hit()

    def update_alien(self):
        # update alien if any alien has reached the screen edge
        for alien in self.aliens.sprites():
            alien.check_edge ()
            alien.update_alien()
        # check the collision between alien and ship
        if pygame.sprite.spritecollideany(self.ship,self.aliens,):
            self.setting.limit-=1
                          
            self.ship_hit()     
       
    def creat_fleet (self):
        # make fleet of aliens
        # create alien adding them in row untill there is not space
        # space between alien is width of alien
        alien = Alien(self)
        fleet_hieght = alien.rect.height
        initial_point = 0
        last_point = 4
        while fleet_hieght<self.setting.screen_width-(10*alien.rect.height):
            position_x = alien.rect.width
            starting_point = 0
            final_point = 12
            while position_x <(self.setting.screen_width-alien.rect.width):
                random_no=randint(starting_point,final_point)
                random_int = randint(initial_point,last_point)
                self.create_new_alien((random_no*100)+position_x,(random_int*92)+fleet_hieght)
                position_x+=2*alien.rect.width
                final_point=final_point-2
                starting_point-=2
            fleet_hieght+=2*alien.rect.height
            last_point-=2
            initial_point-=2

    def create_new_alien(self,position_x,position_y):
        # create new alien
        new_alien = Alien(self)
        new_alien.rect.x = position_x
        new_alien.rect.y = position_y
        self.aliens.add(new_alien)

    def check_keydown(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q :
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullets()
            if self.game_active == True:
                self.gun_shot.play()
            

    def check_keyup(self,event): 
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def check_event(self):
        # method for check input from mouse or keyboard
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.check_keydown(event)
                elif event.type == pygame.KEYUP:
                    self.check_keyup(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.check_play_buttom(mouse_pos)

    def fire_bullets(self):
        # create new bullete and add it to the group
        if len(self.bullete)<self.setting.bullet_allowed:
            new_bullete = Bullet(self)
            self.bullete.add(new_bullete)

    def update_screen(self):
        pygame.display.flip()
        # Set background colour
        self.screen.fill(self.setting.bg_color)
        for bullete in self.bullete.sprites():
            bullete.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.sb.show_score()
        # draw buttom on screen if game is inactive
        if self.game_active == False:
            self.play_buttom.draw_buttom()
            pygame.display.flip()
    def update_bullet(self):
        # get rid of bullet when it reaches top
        for bullet in self.bullete.copy():
            if bullet.rect.bottom<=0:
                self.bullete.remove(bullet)
                # check if bullet hit the alien or not
                # if hit then we get rid out of bullet and alien
            collision = pygame.sprite.groupcollide(self.bullete,self.aliens,True,True)
            if collision:
                for aliens in collision.values():
                    self.stats.score += self.setting.alien_score* len(aliens)
                self.sb.prep_score()
                self.sb.check_high_score()

    def __init__(self):
        '''initialise the game'''  
        pygame.init()
        self.clock = pygame.time.Clock()
        self.setting=Setting()
        self.gun_shot = pygame.mixer.Sound("shot.mp3")
        self.playing_sound = pygame.mixer.Sound("track1.WAV")
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.setting.screen_width = self.screen.get_rect().width
        self.setting.screen_hieght = self.screen.get_rect().height
        pygame.display.set_caption("ALIEN INVASION")
        # create instance of game_state to 
        self.stats = Game_stats (self)
        # create instance of scoreboard
        self.sb = SCORING_SYSTEM(self)
        self.ship = Ship(self)
        self.bullete = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.creat_fleet()
        # start game in active state 
        self.game_active = True
        self.collide = 0
        # make play button
        self.play_buttom = Buttom(self,"PLAY")

    def run_game(self):
        '''Start main loop for the game'''
        while True:
            self.check_event()
            if self.game_active:
                # hide mouse cursor while game is active
                pygame.mouse.set_visible(False)
                self.ship.update()
                self.update_alien()
                self.bullete.update()
                self.update_bullet()
            '''To make the transition of display'''
            self.update_screen()
            self.clock.tick(60)
if __name__ == '__main__':
    game = GAME_ENVIRONMENT()
    game.run_game()
