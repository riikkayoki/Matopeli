import unittest
from services.gameboard import GameBoard


class TestGameboard(unittest.TestCase):
    def setUp(self):
        self.gameboard = GameBoard()

    