import pygame
from ui.styling_ui import UIStyle
from ui.renderer import Renderer

class GameUI:

    """Luokka joka kuvaa pelin graafista käyttöliittymää."""
    
    def __init__(self):

        """Luokan konstruktori"""

        self.display = Renderer(600, 600, (0, 0, 0))
        self.grid_size = 30
        self.style = UIStyle()
        self.clock = pygame.time.Clock()
    
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

    def draw_snake_speed(self, speed):
        self.clock.tick(speed)









        