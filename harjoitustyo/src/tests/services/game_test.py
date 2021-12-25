import unittest
from services.game import Game
from services.points import Points
from entities.snake import Snake
from entities.apple import Apple
from services.points import Points


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.points = Points()
        self.snake = Snake(570, 570)
        self.apple = Apple(570, 570)
        self.points = Points()

    def test_update_points(self):
        self.game.update_points(10, 10, 10, 10)
        get = self.game.points.get_point(10, 10, 10, 10)
        self.assertEqual(get, True)
        self.game.update_points(10, 50, 80, 10)
        get = self.game.points.get_point(10, 50, 80, 10)
        self.assertEqual(get, False)

    def test_gameover(self):
        self.assertEqual(self.game._pause, False)
        self.assertEqual(self.game._start_game, False)
        self.assertEqual(self.game._stop_game, False)
        self.game.game_over(570, 570, [[570, 570]])
        self.assertEqual(self.game._pause, True)
        self.assertEqual(self.game._start_game, False)
        self.assertEqual(self.game._stop_game, True)

    def test_reset(self):
        self.assertEqual(self.game._pause, False)
        self.assertEqual(self.game._start_game, False)
        self.assertEqual(self.game.open_leaderboard, False)
        self.assertEqual(self.game._stop_game, False)
        self.assertEqual(self.game.open_leaderboard, False)
        self.game.reset()
        self.assertEqual(self.game._pause, False)
        self.assertEqual(self.game._start_game, False)
        self.assertEqual(self.game.open_leaderboard, True)
        self.assertEqual(self.points.points, 0)
        self.assertEqual(self.game._stop_game, False)
        self.assertEqual(self.game.open_leaderboard, True)
