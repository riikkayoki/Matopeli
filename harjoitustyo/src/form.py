from ui.userinterface import UserInterface
import pygame


class Form:
    """Luokka, jonka avulla kirjataan pelaajan nimimerkki talteen leaderbordia varten"""
    def __init__(self):
        """Luokan konstruktori"""
        self.display = UserInterface(1000, 720, (0, 0, 0))
        self.enter_rect = pygame.Rect(900, 600, 80, 30)

    def show_form(self):
        with self.display:
            self.display.draw_form()

    def enter(self, mouse):
        if self.enter_rect.collidepoint(mouse):
            return True
        return False


