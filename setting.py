from random import randint
class Setting :
    # class to store all setting of game
    def __init__(self):
        self.screen_hieght = 800
        self.screen_width = 1200
        self.bg_color = (0,0,0)
        # Ship setting
        self.ship_speed = 20
        self.limit = 3
    # Bullet setting
        self.bullet_speed = 20
        self.bullet_hieght = 15
        self.bullet_width = 3
        self.bullet_colour = (60,60,60)
        self.bullet_allowed = 10
    # alien setting
        self.alien_speed = 3
        self.fleet_drop_speed = 0.5
        # 1 represent right and -1 represent 1
        self.fleet_direction = 1
    # scoring setting
        self.alien_score = 50
