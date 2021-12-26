
class GameBoard:
    """A class that represents the gameboard.

    Attributes:
            self.board: a matrix that represents the gameboard"""

    def __init__(self, board_width, board_height, game_area):
        """A constructor of the game that initializes the gameboard.
        Args:
            board_width: width of the gameboard
            board_height: height of the gameboard
            game_area: area of the gameboard."""

        self.board_width, self.board_height, self.game_area = board_width, board_height, game_area
        self.board = [[0 for _ in range(self.board_width)]
                      for _ in range(self.board_height)]
