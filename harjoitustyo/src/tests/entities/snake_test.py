import unittest
import random
from entities.snake import Snake


class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snake = Snake(570, 570)

    def test_turn_snake(self):
        self.assertEqual(self.snake.direction, ('RIGHT' or 'LEFT' or 'DOWN' or 'UP'))

    def test_border_collision(self):
        self.assertEqual(self.snake.position_snake_width == 630, False)
        self.assertEqual(self.snake.position_snake_width == 60, False)
        self.assertEqual(self.snake.position_snake_height == 630, False)
        self.assertEqual(self.snake.position_snake_height == 60, False)

    def test_increase_snake_length(self):
        self.assertEqual(self.snake.length, 1)
        self.snake.increase_snake_length()
        self.assertEqual(self.snake.length, 2)

    def test_snake_collision(self):
        pass

