from harjoitustyo.src.database_connection import get_database_connection
from repositories.leaderboard_repository import LeaderBoardRepository
from ui.styling_ui import UIStyle

class LeaderboardUI:
    def __init__(self, display_width, display_height, display_color):

        """Luokan konstruktori"""

        self.display_width = display_width
        self.display_height = display_height
        self.display_color = display_color
        self.database = LeaderBoardRepository(get_database_connection())
        self.style = UIStyle()

    def draw_leaderboard_headlines(self):
        self.style.text(35, 'LEADERBOARD', self.style.grey, (165, 20))
        self.style.text(23, 'ranking', self.style.grey, (100, 100))
        self.style.text(23, 'username', self.style.grey, (220, 100))
        self.style.text(23, 'points', self.style.grey, (430, 100))

    def draw_leaderboard_results(self):
        results = self.database.find_top10()
        count = 0
        heigth = 0

        for highscores in results:
            count += 1
            heigth += 40
            self.style.text(20, f'{count}', self.style.grey, 
                            (100, 130 + heigth)) 
            self.style.text(20, f'{highscores[0]}', self.style.grey, 
                            (220, 130 + heigth))
            self.style.text(20, f'{highscores[1]}', self.style.grey, 
                            (430, 130 + heigth))
    
    def draw_back_button(self):

        '''Piirtää BACK TO MENU napin.'''
        
        self.style.rect(self.style.grey, (440, 560, 149, 26))
        self.style.text(20, 'BACK TO MENU', self.style.black, (440, 560))
