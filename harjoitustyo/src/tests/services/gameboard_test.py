import unittest
from services.gameboard import GameBoard


class TestGameBoard(unittest.TestCase):
    def setUp(self):
        self.game_board = GameBoard(22, 22, (0, 0, 600, 600))

    def test_board(self):
        self.assertEqual(self.game_board.board, [[0 for _ in range(self.game_board.board_width)]
                                                 for _ in range(self.game_board.board_height)])

    def test_board_width(self):
        self.assertEqual(self.game_board.board_width, 22)
        self.game_board.board_width = 10
        self.assertEqual(self.game_board.board_width, 10)

    def test_board_height(self):
        self.assertEqual(self.game_board.board_height, 22)
        self.game_board.board_height = 10
        self.assertEqual(self.game_board.board_height, 10)

    def test_board_area(self):
        self.assertEqual(self.game_board.game_area, (0, 0, 600, 600))
        self.game_board.game_area = (600, 600, 0, 0)
        self.assertEqual(self.game_board.game_area, (600, 600, 0, 0))
