import unittest
from services.points import Points
from entities.apple import Apple
from entities.snake import Snake
class TestPoints(unittest.TestCase):
    def setUp(self):
        self.points = Points()
        self.snake = Snake(570, 570)
        self.apple = Apple(570, 570)
      

    def test_get_point(self):
        self.assertEqual(self.snake.position_snake_width,
                                 self.snake.position_snake_height,
                                 self.apple.position_apple_width,
                                 self.apple.position_apple_height)
        self.apple.new_random_position()
        self.snake.increase_snake_length()
        self.points += 1
    
    def test_reset_points(self):
        self.assertEqual(self.points.points, 0)

    def test_update_points(self):
        self.points.get_point(self.snake.position_snake_width,
                                 self.snake.position_snake_height,
                                 self.apple.position_apple_width,
                                 self.apple.position_apple_height)
        self.apple.new_random_position()
        self.snake.increase_snake_length()
        self.points.points += 1
        self.assertEqual(self.points.points, 1)