import random


class Apple:

    """A class that represents the apple.

    Attributes:
            self.width: width of the area where the apple can be placed.
            self.height: height of the area where the apple can be placed
            self.position_apple_width: random placement of apple width
            self.position_apple_height: random placement of apple heigth
            self.positions: position of the apple. """

    def __init__(self, width, height):
        """A constructor of the class that defines where the apple can be placed.

        Args:
            width: width of the area where the apple can be placed
            height: heigth of the game board where the apple can be placed.
        """
        self.width = width
        self.height = height
        self.position_apple_width = random.randint(60, self.width)
        self.position_apple_height = random.randint(60, self.height)
        self.positions = [
            [self.position_apple_width, self.position_apple_height]]

    def new_random_position(self):
        """A method that creates random position for the apple."""

        self.position_apple_width = random.randint(60, self.width)
        self.position_apple_height = random.randint(60, self.height)
        self.positions = [self.position_apple_width,
                          self.position_apple_height]
