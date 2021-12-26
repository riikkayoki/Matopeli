import pygame
from ui.styling_ui import UIStyle
from services.renderer import Renderer


class FormUI:
    """A class that represents the form where the user can input the username.

    Attributes:
            self.display: an object that renders the display.
            self.style: an object that brings styling features to the class.
            self.write_rect: the area of text input box.
            self.enter_rect: the area of enter button.
            self.user_text: a string that contains the written text. 
            """

    def __init__(self):
        """A constructor of the class that initializes the form userinterface"""

        self.display = Renderer(600, 600, (200, 200, 200))
        self.style = UIStyle()
        self.write_rect = pygame.Rect(220, 250, 300, 40)
        self.enter_rect = pygame.Rect(220, 300, 80, 30)
        self.user_text = ''

    def show_form(self):
        """A method that brings the objects to the display."""

        with self.display:
            self.draw_gameover_thankyou()
            self.draw_enter_nickname(self.user_text)
            self.draw_enter_button()

    def draw_gameover_thankyou(self):
        """A method that draws the form game over and thank you text."""
        self.style.text(60, 'GAME OVER', self.style.black, (80, 50))
        self.style.text(30, 'Thank you for playing!',
                        self.style.black, (135, 150))

    def draw_enter_nickname(self, user_text):
        """A method that draws the enter nickname text and input box.
        Args:
            user_text: the text that user writes."""

        self.style.text(25, 'Enter nickname: ', self.style.black, (30, 250))
        self.style.rect(self.style.white, (220, 250, 300, 40))
        self.style.rect_borders(self.style.black, (220, 250, 300, 40), 4)
        self.style.text(22, user_text, self.style.black, (230, 255))

    def draw_enter_button(self):
        """A method that draws the enter button."""

        self.style.rect(self.style.black, (220, 300, 80, 30))
        self.style.rect_borders(self.style.white, (220, 300, 80, 30), 1)
        self.style.text(20, 'ENTER', self.style.grey, (227, 303))

    def write(self, mouse):
        """A method that defines when the user clicks the text input box.

        Returns: True if the user clicks the text input box, else False"""

        if self.write_rect.collidepoint(mouse):
            return True
        return False

    def press_enter(self, mouse):
        """A method that defines when the user clicks the enter button.

        Returns: True if the user clicks the enter button, else False"""

        if self.enter_rect.collidepoint(mouse):
            return True
        return False
