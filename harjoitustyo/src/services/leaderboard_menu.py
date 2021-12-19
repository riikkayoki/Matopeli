from ui.userinterface import UserInterface
import pygame

class LeaderBoardMenu:
    """Luokka, jonka avulla luodaan pelille käyttöohje valikko"""
    def __init__(self):
        """Luokan konstruktori"""
        self.display = UserInterface(600, 600, (0, 0, 0))
        self.back_rect = pygame.Rect(440, 560, 149, 26)

    def show_leaderboard(self):
        """Päivittää graafista käyttöliittymää"""
        with self.display:
            self.display.draw_back_button()
            self.display.draw_leaderboard()

    def back(self, mouse):
        """Vie pelaajan takaisin päävalikkoon

        Returns: True, jos painetaan 'Back'-nappia, muussa tapauksessa False"""
        if self.back_rect.collidepoint(mouse):
            return True
        return False
