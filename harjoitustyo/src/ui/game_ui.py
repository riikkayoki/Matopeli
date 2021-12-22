import pygame
from ui.styling_ui import UIStyle

class GameUI:

    """Luokka joka luo graafisen käyttäliittymän"""
    
    def __init__(self, display_width, display_height, display_color):

        """Luokan konstruktori"""

        self.display_width = display_width
        self.display_height = display_height
        self.display_color = display_color
        self.grid_size = 30
        pygame.display.set_mode((self.display_width, display_height))
        self.window = pygame.display.get_surface()
        self.style = UIStyle()

    def __enter__(self):

        """Päivittää pelin taustan"""

        self.window.fill(self.display_color)

    def __exit__(self, exc_type, exc_val, exc_tb):

        """Päivittää näyttöä"""

        pygame.display.update()

    def draw_game_board(self, game_board):

        """Piirtää pelilaudan"""

        for row in range(game_board.board_width):
            for column in range(game_board.board_height):
                self.style.rect(self.style.grey, 
                                (row * self.grid_size, 
                                column * self.grid_size,
                                self.grid_size, self.grid_size))

    def draw_snake(self, snake):

        """Piirtää madon"""

        for position in snake.body:
            self.style.rect(self.style.black, 
                            (position[1], position[0],
                            self.grid_size, self.grid_size))

    def draw_apple(self, apple):

        """Piirtää omenan"""

        for _ in apple.positions:
            self.style.rect(self.style.red, 
                            (apple.position_apple_width, 
                            apple.position_apple_height,
                            self.grid_size, 
                            self.grid_size))

    def draw_points(self, points):

        """Piirtää pisteet"""

        self.style.text(25, f'POINTS: {points}', self.style.black, (460, 10))







        