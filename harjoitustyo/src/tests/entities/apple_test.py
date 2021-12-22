import unittest
from entities.apple import Apple


class TestApple(unittest.TestCase):
    def setUp(self):
        self.apple = Apple(570, 570)

    def test_new_random_position(self):
        self.assertEqual(self.apple.positions, [[self.apple.position_apple_width, self.apple.position_apple_height]])
    
    def test_reset_apple(self):
        self.assertEqual(self.apple.new_random_position(), None)