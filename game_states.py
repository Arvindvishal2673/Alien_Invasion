class Game_stats():
    # class for track stats
    def __init__(self,ai_game):
        # high score 
        self.high_score = 0
        #initializes statstics
        self.setting = ai_game.setting
        self.reset_stats()
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
       
        self.score = 0

