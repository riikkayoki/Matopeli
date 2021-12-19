
class GameBoard:
    """Luokka, jonka avulla luodaan pelilauta

    Attributes:
        self.board_width = pelilaudan leveys
        self.board_height = pelilaudan pituus
        self.game_area = pelialue
        self.board = pelilauta
        """
    def __init__(self, board_width, board_height, game_area):
        """Luokan konstruktori"""
        self.board_width, self.board_height, self.game_area = board_width, board_height, game_area
        self.board = [[0 for _ in range(self.board_width)]
                      for _ in range(self.board_height)]