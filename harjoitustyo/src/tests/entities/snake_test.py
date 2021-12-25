import unittest
from entities.snake import Snake


class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snake = Snake(570, 570)

    def test_turn_snake(self):
        self.assertTrue(self.snake.direction, 'RIGHT')
        self.assertTrue(self.snake.direction, 'UP')
        self.assertTrue(self.snake.direction, 'LEFT')
        self.assertTrue(self.snake.direction, 'DOWN')

    def test_move_snake(self):
        self.snake.turn_snake(self.snake.direction)
        self.snake.move_snake()
        self.assertTrue(self.snake.position_snake_height >=
                        60 and self.snake.position_snake_height <= self.snake.height)
        self.assertTrue(self.snake.position_snake_width >=
                        60 and self.snake.position_snake_width <= self.snake.width)

    def test_increase_snake_length(self):
        self.assertEqual(self.snake.length, 0)
        self.snake.increase_snake_length()
        self.assertEqual(self.snake.length, 1)

    def test_border_collision(self):
        self.assertEqual(self.snake.border_collision(10, 10), False)
        self.assertEqual(self.snake.border_collision(570, 570), True)
        self.assertEqual(self.snake.border_collision(570, 10), True)
        self.assertEqual(self.snake.border_collision(0, 570), True)
        self.assertEqual(self.snake.border_collision(0, 10), True)
        self.assertEqual(self.snake.border_collision(10, 570), True)

    def test_snake_collision(self):
        if self.snake.snake_collision(self.snake.body):
            self.assertEqual(self.snake.body[0] in self.snake.body[60:], True)
        else:
            self.assertEqual(self.snake.body[0] in self.snake.body[60:], False)

    def test_reset_snake(self):
        self.snake.reset_snake()
        self.assertTrue(self.snake.position_snake_height >=
                        60 and self.snake.position_snake_height <= self.snake.height)
        self.assertTrue(self.snake.position_snake_width >=
                        60 and self.snake.position_snake_width <= self.snake.width)
        self.snake.turn_snake(self.snake.direction)
        self.snake.move_snake()
