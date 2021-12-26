import pygame


class Renderer:
    """A class that represents the handlement of rendering in the game."""

    def __init__(self, display_width, display_height, display_color):
        """A constructor that creates the pygame display.
        Args:
            display_width: an object that defines the display width.
            display_height: an object that defines the display height.
            display_color: an object that defines the display color."""

        self.display_width = display_width
        self.display_height = display_height
        self.display_color = display_color
        pygame.display.set_mode((self.display_width, display_height))
        self.window = pygame.display.get_surface()

    def __enter__(self):
        """A method to fill the surface color to the display."""

        self.window.fill(self.display_color)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """A method to update the display."""

        pygame.display.update()
