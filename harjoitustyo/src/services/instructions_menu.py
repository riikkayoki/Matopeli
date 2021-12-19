from ui.userinterface import UserInterface
import pygame

class InstructionsMenu:
    """Luokka, jonka avulla luodaan pelille käyttöohje valikko"""
    def __init__(self):
        """Luokan konstruktori"""
        self.display = UserInterface(600, 600, (0, 0, 0))
    
    def show_instructions(self):
        """Päivittää graafista käyttöliittymää"""
        with self.display:
            self.display.draw_back_button()
            self.display.draw_instructions()

   

