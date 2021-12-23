import unittest
from services.points import Points
from entities.apple import Apple
from entities.snake import Snake

class TestPoints(unittest.TestCase):
    def setUp(self):
        self.points = Points()
        self.snake = Snake(570, 570)
        self.apple = Apple(570, 570)
   

    def test_points(self):
        self.assertEqual(self.points.points, 0)
        self.points.points += 1
        self.assertEqual(self.points.points, 1)
        getpoint = self.points.get_point(self.snake.position_snake_width, self.snake.position_snake_height,
                  self.apple.position_apple_width, self.apple.position_apple_height)
        if getpoint == True:
            self.assertEqual(self.points.points, 2)
            


