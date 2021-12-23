import pygame
from ui.styling_ui import UIStyle
from ui.renderer import Renderer

class MainMenu:

    '''Luokka, joka kuvaa päävalikon grafiikkaa.
    
    Attributes:
            self.style: Olio, jolla on UIStyle -luokkaa vastaavat metodit.
            '''

    def __init__(self):

        """Luokan konstruktori"""
       
        self.style = UIStyle()
        self.display = Renderer(600, 600, (0, 0, 0))
        self.start_rect = pygame.Rect((self.display.display_width // 4) + 20, 200, 250, 50)
        self.instruction_rect = pygame.Rect(self.display.display_width // 4 - 2, 400, 290, 50)
        self.leaderboard_rect = pygame.Rect(self.display.display_width // 4 - 5, 300, 300, 50)
        self.back_rect = pygame.Rect(440, 560, 149, 26)
    
    def run_main_menu(self):

        '''Päivittää päävalikon graafista käyttöliityymää'''

        with self.display:
            self.draw_menu_text()
            self.draw_start_button()
            self.draw_instruction_button()
            self.draw_leaderboard_button()
 
    def draw_menu_text(self):

        '''Piirtää 'Main Menu' tekstin päävalikkoon'''

        self.style.text(70, 'MAIN MENU', self.style.grey, (self.display.display_width // 4 - 50, 80))


    def draw_start_button(self):

        '''Piirtää 'Start' -napin päävalikkoon'''

        self.style.button(self.style.grey, 
                        (self.display.display_width // 4 + 18, 200, 258, 50), 
                        self.style.white, 5, 40, 'START GAME', 
                        self.style.black, (self.display.display_width // 4 + 22, 200))

    def draw_leaderboard_button(self):

        '''Piirtää 'Leaderboard' -napin päävalikkoon'''

        self.style.button(self.style.grey, 
                        (self.display.display_width // 4 - 12, 300, 310, 50), 
                        self.style.white, 5, 40, 'LEADERBOARD', 
                        self.style.black, (self.display.display_width // 4 - 5, 300))

    def draw_instruction_button(self):

        '''Piirtää 'Instructions' -napin päävalikkoon'''

        self.style.button(self.style.grey, 
                        (self.display.display_width // 4 - 8, 397, 300, 50), 
                        self.style.white, 5, 40, 'INSTRUCTIONS', 
                        self.style.black, (self.display.display_width // 4 - 2, 400))

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



