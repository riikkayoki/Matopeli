import unittest
from entities.snake import Snake


class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snake = Snake(570, 570)

    def test_directions(self):
        self.assertEqual(self.snake.directions, {'RIGHT': (0, 1), 'LEFT': (0, -1),
                           'UP': (-1, 0), 'DOWN': (1, 0)})

    def test_turn_snake(self):
        self.assertTrue(self.snake.direction, 'RIGHT')
        self.assertTrue(self.snake.direction, 'UP')
        self.assertTrue(self.snake.direction, 'LEFT')
        self.assertTrue(self.snake.direction, 'DOWN')
  
    def test_border_collision(self):
        if self.snake.border_collision():
            self.assertEqual(self.snake.position_snake_width == 570, True)
            self.assertEqual(self.snake.position_snake_width == 60, True)
            self.assertEqual(self.snake.position_snake_height == 570, True)
            self.assertEqual(self.snake.position_snake_height == 60, True)
        else:
            self.assertEqual(self.snake.position_snake_width == 570, False)
            self.assertEqual(self.snake.position_snake_width == 60, False)
            self.assertEqual(self.snake.position_snake_height == 570, False)
            self.assertEqual(self.snake.position_snake_height == 60, False)

    def test_increase_snake_length(self):
        self.snake.increase_snake_length()
        self.assertEqual(self.snake.length, 1)

    def test_snake_collision(self):
        if self.snake.snake_collision():
            self.assertEqual(self.snake.body[0] == self.snake.body[60:], True)
        else:
            self.assertEqual(self.snake.body[0] == self.snake.body[60:], False)

    def test_snake_body(self):
        self.assertEqual(self.snake.body, [[self.snake.position_snake_width, self.snake.position_snake_height]])
    
    def test_snake_positions(self):
        self.assertTrue(self.snake.position_snake_height >= 60 and self.snake.position_snake_height <= self.snake.height)
        self.assertTrue(self.snake.position_snake_width >= 60 and self.snake.position_snake_width <= self.snake.width)
    
    def test_width(self):
        self.assertEqual(self.snake.width, 570)
    
    def test_height(self):
        self.assertEqual(self.snake.height, 570)

   



