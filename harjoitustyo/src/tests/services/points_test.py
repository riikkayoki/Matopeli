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
        point = self.points.get_point(100, 10, 40, 80)
        self.assertEqual(point, False)

    def test_points(self):
        self.points.points = 0
        self.assertEqual(self.points.points, 0)
        self.points.points += 1
        self.assertEqual(self.points.points, 1)

    def test_reset_points(self):
        self.points.reset_points()
        self.assertEqual(self.points.points, 0)
