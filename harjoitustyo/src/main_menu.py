import pygame
from ui.userinterface import UserInterface

class MainMenu:
    """Luokka, jonka avulla luodaan pelille päävalikko"""
    def __init__(self):
        """Luokan konstruktori"""
        self.display = UserInterface(1000, 720, (0, 0, 0))
        self.start_rect = pygame.Rect((self.display.display_width // 3) + 25, 250, 250, 50)
        self.instruction_rect = pygame.Rect(self.display.display_width // 3, 350, 300, 50)

    def main_menu(self):
        """Päivittää päävalikon graafista käyttöliityymää"""
        with self.display:
            self.display.draw_menu_text()
            self.display.draw_start_button()
            self.display.draw_instruction_button()

    def start(self, mouse):
        """Aloittaa pelin

        Returns: True, jos painetaan 'Start'-nappia, muussa tapauksessa False"""
        if self.start_rect.collidepoint(mouse):
            return True
        return False

    def instructions(self, mouse):
        """Avaa käyttöohjeikkunan

        Returns: True, jos painetaan 'Instructions'-nappia, muussa tapauksessa False"""
        if self.instruction_rect.collidepoint(mouse):
            return True
        return False





