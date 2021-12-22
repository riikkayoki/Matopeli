import unittest
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
        self.snake.increase_snake_length()

    def test_snake_collision(self):
        self.assertEqual(self.snake.body[0] == self.snake.body[60:], False)
    
    def test_reset_snake(self):
        self.assertEqual(self.snake.body, [[self.snake.position_snake_width, self.snake.position_snake_height]])
        self.assertEqual(self.snake.turn_snake(self.snake.direction), None)
        self.assertEqual(self.snake.move(), None)

    def test_game_over(self):
        self.assertEqual(self.snake.border_collision(), False)
        self.assertEqual(self.snake.snake_collision(), False)
        