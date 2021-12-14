from ui.userinterface import UserInterface
import pygame

class InstructionsMenu:
    """Luokka, jonka avulla luodaan pelille käyttöohje valikko"""
    def __init__(self):
        """Luokan konstruktori"""
        self.display = UserInterface(1000, 720, (0, 0, 0))
        self.back_rect = pygame.Rect(900, 600, 300, 50)

    def show_instructions(self):
        with self.display:
            self.display.draw_back_button()
            self.display.draw_instructions()

    def back(self, mouse):
        if self.back_rect.collidepoint(mouse):
            return True
        return False


