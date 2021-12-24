import unittest
from services.game import Game
from services.points import Points
from entities.snake import Snake
from entities.apple import Apple
from services.clock import Clock

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.points = Points()
        self.snake = Snake(570, 570)
        self.apple = Apple(570, 570)

    def test_reset_game(self):
        self.game.reset_game()
        self.assertEqual(self.game.reset_game(), self.game.reset_game())

    def test_update_points(self):
        self.game.update_points(10, 10, 10, 10)
        get = self.game.points.get_point(10, 10, 10, 10)
        self.assertEqual(get, True)
        self.game.update_points(10, 50, 80, 10)
        get = self.game.points.get_point(10, 50, 80, 10)
        self.assertEqual(get, False)

    def test_game_over(self):
        self.game.game_over()
        self.assertEqual(self.game.reset_game(), self.game.reset_game())
        if self.snake.border_collision() or self.snake.snake_collision():
            self.assertFalse(self.game.start_game)
            self.assertTrue(self.game.stop_game)
            self.assertTrue(self.game.pause)

           

