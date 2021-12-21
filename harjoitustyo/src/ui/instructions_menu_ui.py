import pygame
from styling_ui import UIStyle

class InstructionsUI:

    '''Luokka, joka kuvaa käyttöohje valikon grafiikkaa.
    
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

    def draw_instructions(self):

        '''Piirtää käyttöohjeet'''

        self.style.text(25, 'Eat the apples, but do not hit the walls or your own tail!',
        self.style.grey, (20, 250))

    def draw_back_button(self):

        '''Piirtää BACK TO MENU -napin'''

        self.style.button(self.style.grey, (440, 560, 149, 26), 2, 
                            self.style.white, 20, 'BACK TO MENU', 
                            self.style.black, (430, 540))