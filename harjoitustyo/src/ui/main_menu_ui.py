import pygame
from ui.styling_ui import UIStyle
from services.renderer import Renderer


class MainMenu:
    """A class that represents the main menu.

    Attributes:
            self.style: an object that imports styling features to the class.
            self.display: an object that renders the display.
            self.start_rect: the area of start -button
            self.instruction_rect: the area of instruction -button
            self.leaderboard_rect: the area of leaderboard_button
            self.back_rect: the area of back to menu -button"""

    def __init__(self):
        """A constructor of the class that initializes the menu userinterface."""

        self.style = UIStyle()
        self.display = Renderer(600, 600, (0, 0, 0))
        self.start_rect = pygame.Rect(
            (self.display.display_width // 4) + 20, 200, 250, 50)
        self.instruction_rect = pygame.Rect(
            self.display.display_width // 4 - 2, 400, 290, 50)
        self.leaderboard_rect = pygame.Rect(
            self.display.display_width // 4 - 5, 300, 300, 50)
        self.back_rect = pygame.Rect(440, 560, 149, 26)

    def show_main_menu(self):
        """A method that brings the objects to the display."""

        with self.display:
            self.draw_menu_text()
            self.draw_start_button()
            self.draw_instruction_button()
            self.draw_leaderboard_button()

    def draw_menu_text(self):
        """A method to draw the headline text."""

        self.style.text(70, 'MAIN MENU', self.style.grey,
                        (self.display.display_width // 4 - 50, 80))

    def draw_start_button(self):
        """A method to draw the start -button."""

        self.style.button(self.style.grey,
                          (self.display.display_width // 4 + 18, 200, 258, 50),
                          self.style.white, 5, 40, 'START GAME',
                          self.style.black, (self.display.display_width // 4 + 22, 200))

    def draw_leaderboard_button(self):
        """A method to draw the leaderboard -button."""
        self.style.button(self.style.grey,
                          (self.display.display_width // 4 - 12, 300, 310, 50),
                          self.style.white, 5, 40, 'LEADERBOARD',
                          self.style.black, (self.display.display_width // 4 - 5, 300))

    def draw_instruction_button(self):
        """A method to draw the instruction -button."""
        self.style.button(self.style.grey,
                          (self.display.display_width // 4 - 8, 397, 300, 50),
                          self.style.white, 5, 40, 'INSTRUCTIONS',
                          self.style.black, (self.display.display_width // 4 - 2, 400))

    def to_start(self, mouse):
        """A method that defines when the user clicks the start -button.

        Returns: True if the user clicks the button, else False"""

        if self.start_rect.collidepoint(mouse):
            return True
        return False

    def to_instructions(self, mouse):
        """A method that defines when the user clicks the instruction button.

        Returns: True if the user clicks the button, else False"""

        if self.instruction_rect.collidepoint(mouse):
            return True
        return False

    def to_leaderboard(self, mouse):
        """A method that defines when the user clicks the leaderboard -button.

        Returns: True if the user clicks the button, else False"""

        if self.leaderboard_rect.collidepoint(mouse):
            return True
        return False

    def back(self, mouse):
        """A method that defines when the user clicks the back -button.

        Returns: True if the user clicks the button, else False"""

        if self.back_rect.collidepoint(mouse):
            return True
        return False
