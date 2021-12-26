from ui.styling_ui import UIStyle


class GameUI:
    """A class that represents the game objects that will be shown on pygame window.

    Attributes:
            self.grid_size: the grid size of the game.
            self.style: an object that brings the styling features to the game
            """

    def __init__(self):
        """A constructor of the class that initializes the game userinterface."""

        self.grid_size = 30
        self.style = UIStyle()

    def draw_game_board(self, game_board):
        """A method to draw the gameboard.
        Args:
            game_board: the gameboard"""

        for row in range(game_board.board_width):
            for column in range(game_board.board_height):
                self.style.rect(self.style.grey,
                                (row * self.grid_size,
                                 column * self.grid_size,
                                 self.grid_size, self.grid_size))

    def draw_snake(self, snake):
        """A method to draw the snake.
        Args:
            snake: the snake"""

        for position in snake.body:
            self.style.rect(self.style.black,
                            (position[1], position[0],
                             self.grid_size, self.grid_size))

    def draw_apple(self, apple):
        """A method to draw the apple.
        Args:
            apple: the apple"""

        for _ in apple.positions:
            self.style.rect(self.style.red,
                            (apple.position_apple_width,
                             apple.position_apple_height,
                             self.grid_size,
                             self.grid_size))

    def draw_points(self, points):
        """A method to draw the points.
        Args:
            points: the points during the game."""

        self.style.text(25, f'POINTS: {points}', self.style.black, (460, 10))
