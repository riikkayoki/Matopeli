from typing_extensions import ParamSpecArgs
import unittest
from services.game import Game
from services.points import Points
from entities.snake import Snake
from entities.apple import Apple

game = Game()

class Game(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.points = Points()
        self.snake = Snake(570, 570)
        self.apple = Apple(570, 570)
    
    def test_update_points(self):
        self.points.get_point(self.snake.position_snake_width,
                                 self.snake.position_snake_height,
                                 self.apple.position_apple_width,
                                 self.apple.position_apple_height)
        self.assertEqual(self.points.points, 0)

    def test_game_over(self):
        pass
      
    def test_reset_game(self):
        pass
        