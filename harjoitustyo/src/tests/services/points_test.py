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
        points = self.points.get_point(10, 10, 10, 10)
        self.assertEqual(points, True)

    def test_points(self):
        self.points.points += 1
        self.assertEqual(self.points.points, 1)