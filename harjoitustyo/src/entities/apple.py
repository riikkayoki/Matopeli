import random


class Apple:

    """Luokka, joka kuvaa omenaa.

    Attributes:
            self.width: pelilaudan leveys, johon omenan voi sijoittaa.
            self.height: pelilaudan pituus, johon omenan voi sijoittaa"""

    def __init__(self, width, height):

        """Luokan konstruktori"""

        self.width = width
        self.height = height
        self.position_apple_width = random.randint(60, self.width)
        self.position_apple_height = random.randint(60, self.height)
        self.positions = [
            [self.position_apple_width, self.position_apple_height]]

    def new_random_position(self):

        self.position_apple_width = random.randint(60, self.width)
        self.position_apple_height = random.randint(60, self.height)
        self.positions = [self.position_apple_width,
                          self.position_apple_height]
