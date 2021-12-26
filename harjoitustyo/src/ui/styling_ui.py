import pygame
from services.renderer import Renderer


class UIStyle:
    """A class that represents the styling features.

    Attributes:
        self.grey: grey color object
        self.black: black color object
        self.white: white color object
        self.red: red color object
        self.render: an object that renders the display
        self.window: an object that references to the currently set display surface
    """

    def __init__(self):
        """A class constructor that initializes the pygame styling features."""

        self.grey = (200, 200, 200)
        self.black = (0, 0, 0)
        self.white = (250, 250, 250)
        self.red = (200, 0, 0)
        self.render = Renderer(600, 600, (0, 0, 0))
        self.window = self.render.window

    def text(self, font_size, text, color, location):
        """A method that defines the text styling features.

        Args:
            font_size: a font size of the text.
            text: text string
            color: a color of the text
            location: a location of the text"""

        font = pygame.font.SysFont('Times New Roman', font_size)
        text = font.render(text, False, color)
        self.render.window.blit(text, location)

    def rect(self, color, area):
        """A method that defines the rectangle features.

        Args:
            color: a color of the rectangle
            area: an area of the rectangle"""

        pygame.draw.rect(self.window, color, pygame.Rect(area))

    def rect_borders(self, color, area, size):
        """A method that defines the border line for the rectangles.

        Args:
            color: the line color
            area: an area of the line
            size: thickness of the line"""

        pygame.draw.rect(self.window, color, pygame.Rect(area), size)

    def button(self, rect_color, area, border_color, line_size, text_size,
               text, text_color, text_location):
        """A method that defines the button features.

        Args:
            rect_color: a color of the rectangle
            area: an area of the rectangle
            border_color: a color of the border line
            line_size: a thickness of the line
            text_size: the text size
            text: text string
            text_color: a color of the text
            text_location: a location of the text"""

        self.rect(rect_color, area)
        self.rect_borders(border_color, area, line_size)
        self.text(text_size, text, text_color, text_location)
