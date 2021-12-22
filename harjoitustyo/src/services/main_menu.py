import pygame
from ui.main_menu_ui import MainMenuUI

class MainMenu:

    '''Luokka, joka kuvaa pelin päävalikkoa.
    
    Attributes:
        
    '''

    def __init__(self):

        '''Luokan konstruktori, joka luo päävalikon.'''

        self.display = MainMenuUI(600, 600, (0, 0, 0))
        self.start_rect = pygame.Rect((self.display.display_width // 4) + 20, 200, 250, 50)
        self.instruction_rect = pygame.Rect(self.display.display_width // 4 - 2, 400, 290, 50)
        self.leaderboard_rect = pygame.Rect(self.display.display_width // 4 - 5, 300, 300, 50)
        self.back_rect = pygame.Rect(440, 560, 149, 26)

    def run_main_menu(self):

        '''Päivittää päävalikon graafista käyttöliityymää'''

        with self.display:
            self.display.draw_menu_text()
            self.display.draw_start_button()
            self.display.draw_instruction_button()
            self.display.draw_leaderboard_button()

    def to_start(self, mouse):

        '''Aloittaa pelin, jos pelaaja painaa start nappia. 

        Args:
            mouse: Hiiren klikkauksen sijainti.

        Returns: True, jos painetaan 'Start'-nappia, muussa tapauksessa False'''

        if self.start_rect.collidepoint(mouse):
            return True
        return False

    def to_instructions(self, mouse):

        '''Avaa käyttöohjeikkunan, kun pelaaja painaa instructions nappia.

        Args:
            mouse: Hiiren klikkauksen sijainti.

        Returns: True, jos painetaan 'Instructions'-nappia, muussa tapauksessa False'''

        if self.instruction_rect.collidepoint(mouse):
            return True
        return False
    
    def to_leaderboard(self, mouse):

        '''Avaa tulostaulukon, kun pelaaja painaa leaderboard nappia.

        Args:
            mouse: Hiiren klikkauksen sijainti.

        Returns: True, jos painetaan 'Leaderboard'-nappia, muussa tapauksessa False'''

        if self.leaderboard_rect.collidepoint(mouse):
            return True
        return False

    def back(self, mouse):

        '''Vie pelaajan takaisin päävalikkoon instruction- ja leaderboard -menusta, 
            jos pelaaja painaa back to menu nappia.

        Args:
            mouse: Hiiren klikkauksen sijainti.

        Returns: True, jos painetaan 'Back'-nappia, muussa tapauksessa False'''
        
        if self.back_rect.collidepoint(mouse):
            return True
        return False



