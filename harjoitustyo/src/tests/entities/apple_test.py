import unittest
from entities.apple import Apple


class TestApple(unittest.TestCase):
    def setUp(self):
        self.apple = Apple(570, 570)

    def test_apple_positions(self):
        self.assertTrue(self.apple.positions, [self.apple.position_apple_width,
                                               self.apple.position_apple_height])

    def test_random_apple_position(self):
        self.apple.new_random_position()
        width = self.apple.position_apple_width >= 60 and \
            self.apple.position_apple_width <= self.apple.width
        height = self.apple.position_apple_height >= 60 and \
            self.apple.position_apple_height <= self.apple.height
        self.assertTrue(width)
        self.assertTrue(height)
