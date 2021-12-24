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
        self.points.get_point(self.snake.position_snake_width,
                              self.snake.position_snake_height,
                              self.apple.position_apple_width,
                              self.apple.position_apple_height)
        self.assertEqual(abs(self.snake.position_snake_width - self.apple.position_apple_height) <= 20
                         and abs(self.snake.position_snake_height - self.apple.position_apple_width <= 20), False)

    def test_points(self):
        self.points.reset_points()
        self.assertTrue(self.points.points == 0)