import unittest
from repositories.snake import Snake


class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snake = Snake()

    def test_turn_snake(self):
        self.assertEqual(self.snake.direction, 'RIGHT')
