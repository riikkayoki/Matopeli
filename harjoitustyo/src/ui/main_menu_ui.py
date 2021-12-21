import pygame
from styling_ui import UIStyle

class MainMenuUI:

    '''Luokka, joka kuvaa päävalikon grafiikkaa.
    
    Attributes:
            self.style: Olio, jolla on UIStyle -luokkaa vastaavat metodit.
            '''

    def __init__(self, display_width, display_height, display_color):

        """Luokan konstruktori"""

        self.display_width = display_width
        self.display_height = display_height
        self.display_color = display_color
        self.window = pygame.display.get_surface()
        self.style = UIStyle()
    
    def __enter__(self):

        '''Päivittää näytön taustan'''

        self.window.fill(self.display_color)

    def __exit__(self, exc_type, exc_val, exc_tb):

        '''Päivittää näyttöä'''
        pygame.display.update()
     

    def draw_menu_text(self):

        '''Piirtää 'Main Menu' tekstin päävalikkoon'''

        self.style.text(70, 'MAIN MENU', self.style.grey, (self.display_width // 4 - 50, 80))


    def draw_start_button(self):

        '''Piirtää 'Start' -napin päävalikkoon'''

        self.style.button(self.style.grey, 
                        (self.display_width // 4 + 18, 200, 258, 50), 
                        self.style.white, 5, 40, 'START GAME', 
                        self.style.black, (self.display_width // 4 + 22, 200))

    def draw_leaderboard_button(self):

        '''Piirtää 'Leaderboard' -napin päävalikkoon'''

        self.style.button(self.style.grey, 
                        (self.style.display_width // 4 - 12, 300, 310, 50), 
                        self.style.grey, 5, 40, 'LEADERBOARD', 
                        self.style.black, (self.display_width // 4 - 5, 300))

    def draw_instruction_button(self):

        '''Piirtää 'Instructions' -napin päävalikkoon'''

        self.style.button(self.style.grey, 
                        (self.display_width // 4 - 8, 397, 300, 50), 
                        self.style.grey, 5, 40, 'INSTRUCTIONS', 
                        self.style.black, (self.display_width // 4 - 2, 400))


