import pygame
from ui.styling_ui import UIStyle
from services.gameboard import GameBoard
from entities.snake import Snake
from entities.apple import Apple
from services.points import Points
from ui.renderer import Renderer

class GameUI:

    """Luokka joka kuvaa pelin graafista käyttöliittymää."""
    
    def __init__(self):

        """Luokan konstruktori"""

        self.display = Renderer(600, 600, (0, 0, 0))
        self.grid_size = 30
        self.style = UIStyle()
        self.game_board = GameBoard(22, 22, pygame.Rect(0, 0, 600, 600))
        self.snake = Snake(570, 570)
        self.apple = Apple(570, 570)
        self.points = Points()

    def run_game(self):
        with self.display:
            self.snake.move()
            self.points.update_points()
            self.snake.game_over()
            self.draw_game_board(self.game_board)
            self.draw_apple(self.apple)
            self.draw_snake(self.snake)
            self.draw_points(self.points.points)
    
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







        