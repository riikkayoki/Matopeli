import unittest
from entities.apple import Apple
from random import Random
random = Random()


class TestApple(unittest.TestCase):
    def setUp(self):
        global random
        random = Random(600)
        self.apple = Apple(570, 570)

    def test_random_positions(self):
        self.assertTrue(self.apple.position_apple_width >=
                        60 and self.apple.position_apple_width <= self.apple.width)
        self.assertTrue(self.apple.position_apple_height >=
                        60 and self.apple.position_apple_height <= self.apple.height)

    def test_give_random_positions(self):
        position_apple_width = random.randint(60, self.apple.width)
        position_apple_height = random.randint(60, self.apple.height)
        self.assertTrue(self.apple.positions, [position_apple_width,
                                               position_apple_height])

    def test_random_apple_position(self):
        self.apple.new_random_position()
        width = self.apple.position_apple_width >= 60 and self.apple.position_apple_width <= self.apple.width
        height = self.apple.position_apple_height >= 60 and self.apple.position_apple_height <= self.apple.height
        self.assertTrue(width)
        self.assertTrue(height)
        self.assertEqual(self.apple.positions, [
                         self.apple.position_apple_width, self.apple.position_apple_height])

    def test_apple_position(self):
        self.assertEqual(self.apple.positions, [
                         [self.apple.position_apple_width, self.apple.position_apple_height]])

    def test_width(self):
        self.assertEqual(self.apple.width, 570)
        self.apple.width = 600
        self.assertEqual(self.apple.width, 600)

    def test_heigth(self):
        self.assertEqual(self.apple.height, 570)
        self.apple.height = 600
        self.assertEqual(self.apple.height, 600)
