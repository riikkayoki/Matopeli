import pygame
from database_connection import get_database_connection
from repositories.leaderboard_repository import LeaderBoardRepository
from ui.styling_ui import UIStyle

class LeaderboardMenuUI:
    def __init__(self, display_width, display_height, display_color):

        """Luokan konstruktori"""

        self.display_width = display_width
        self.display_height = display_height
        self.display_color = display_color
        self.database = LeaderBoardRepository(get_database_connection())
        pygame.display.set_mode((self.display_width, display_height))
        self.window = pygame.display.get_surface()
        self.style = UIStyle()
    
    def __enter__(self):

        '''Päivittää näytön taustan'''

        self.window.fill(self.display_color)

    def __exit__(self, exc_type, exc_val, exc_tb):

        '''Päivittää näyttöä'''
        pygame.display.update()

    def draw_leaderboard_headlines(self):
        self.style.text(30, 'LEADERBOARD', self.style.grey, (180, 25))
        self.style.text(23, 'ranking', self.style.grey, (100, 95))
        self.style.text(23, 'username', self.style.grey, (220, 95))
        self.style.text(23, 'points', self.style.grey, (430, 95))

    def draw_leaderboard_results(self):
        results = self.database.find_top10()
        count = 0
        heigth = 0

        for highscores in results:
            count += 1
            heigth += 35
            self.style.text(20, f'{count}', self.style.grey, 
                            (125, 105 + heigth)) 
            self.style.text(20, f'{highscores[0]}', self.style.grey, 
                            (222, 105 + heigth))
            self.style.text(20, f'{highscores[1]}', self.style.grey, 
                            (455, 105 + heigth))
    
    def draw_back_button(self):

        '''Piirtää BACK TO MENU -napin'''

        self.style.button(self.style.grey, (426, 550, 155, 30), 
                            self.style.white, 
                            2, 20, 'BACK TO MENU', 
                            self.style.black, (430, 553))