
class GameBoard:

    def __init__(self, board_width, board_height, game_area):
        self.board_width, self.board_height, self.game_area = board_width, board_height, game_area
        self.board = [[0 for _ in range(self.board_width)]
                      for _ in range(self.board_height)]

