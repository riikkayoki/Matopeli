from harjoitustyo.src.ui.game_ui import UserInterface
import pygame

class InstructionsMenu:

    '''Luokka, joka kuvaa käyttöohjevalikkoa.
    
    Attributes:
            self.display: Olio, jolla on UserInterface-luokkaa vastaavat metodit.
    '''

    def __init__(self):

        '''Luokan konstruktori, joka luo käyttöohjevalikon pelille'''

        self.display = UserInterface(600, 600, (0, 0, 0))
    
    def show_instructions(self):

        '''Päivittää graafista käyttöliittymää'''

        with self.display:
            self.display.draw_back_button()
            self.display.draw_instructions()

   

