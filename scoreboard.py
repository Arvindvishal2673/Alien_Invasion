import pygame.font
from pygame.sprite import Group
from ship import Ship

class SCORING_SYSTEM:
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.setting
        self.stats = ai_game.stats
        self.text_colour = (0, 150, 0)
        self.font = pygame.font.SysFont(None, 60)
        self.prep_score()
        self.prep_ships()
        # prepare the initial score image
        self.prep_high_score()
    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True,
        self.text_colour, self.settings.bg_color)
        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        
    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        ship_width = 80  # Adjust the new width as needed
        ship_height = 80  # Adjust the new height as needed
        for ship_number in range(self.settings.limit):
            ship = Ship(self.ai_game)
            ship.image = pygame.transform.scale(ship.image, (ship_width, ship_height))
            ship.rect = ship.image.get_rect()
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """Draw scores, level, and ships to the screen."""
        self.screen.blit(self.score_img, self.score_rect)
        self.ships.draw(self.screen)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = str(self.stats.score)
        self.score_img = self.font.render(score_str, True, self.text_colour, self.settings.bg_color)
        # Display the score at the top right of the screen
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        

