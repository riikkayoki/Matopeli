import pygame
from ui.styling_ui import UIStyle
from ui.renderer import Renderer

class InstructionsUI:

    '''Luokka, joka kuvaa käyttöohje valikon grafiikkaa.
    
    Attributes:
            self.style: Olio, jolla on UIStyle -luokkaa vastaavat metodit.
            '''

    def __init__(self):

        """Luokan konstruktori"""

        self.display = Renderer(600, 600, (0, 0, 0))
        self.style = UIStyle()

    def run_instructions_menu(self):

        '''Päivittää graafista käyttöliittymää'''

        with self.display:
            self.draw_back_button()
            self.draw_instructions()

    def draw_instructions(self):

        '''Piirtää käyttöohjeet'''

        self.style.text(25, 'Eat the apples, but do not hit the walls or your own tail!',
        self.style.grey, (20, 250))

    def draw_back_button(self):

        '''Piirtää BACK TO MENU -napin'''

        self.style.button(self.style.white, (426, 550, 155, 30), self.style.grey, 
                            2, 20, 'BACK TO MENU', 
                            self.style.black, (430, 553))
