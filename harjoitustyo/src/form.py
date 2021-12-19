from ui.userinterface import UserInterface
import pygame


class Form:
    """Luokka, jonka avulla kirjataan pelaajan nimimerkki talteen leaderbordia varten"""
    def __init__(self):
        """Luokan konstruktori"""
        self.display = UserInterface(600, 600, (200, 200, 200))
        self.write_rect = pygame.Rect(220, 250, 300, 40)
        self.enter_rect = pygame.Rect(220, 300, 80, 30)
 

    def form(self):
        """Päivittää graafista käyttöliityymää"""

        with self.display:
            self.display.draw_form()
            self.display.draw_input_box()
            self.display.draw_enter_button()

    def write(self, mouse):
        if self.write_rect.collidepoint(mouse):
            return True
        return False
    
    def press_enter(self, mouse):
        if self.enter_rect.collidepoint(mouse):
            return True
        return False



