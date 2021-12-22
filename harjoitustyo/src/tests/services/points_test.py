import unittest
from services.points import Points

class TestPoints(unittest.TestCase):
    def setUp(self):
        self.points = Points()

    def test_get_point(self, snake_position_width, snake_position_height,
                  apple_position_width, apple_position_height):

        pass
    
    def test_reset_points(self):
        self.assertEqual(self.points, 0)

    def test_update_points(self):
        pass