import random

class Apple:
    """Luokka, joka kuvaa syötävää omenaa

    Attributes:
        self.width = omenan pituus
        self.height = omenan leveys
        self.position_apple_width = annetaan omenan pituudelle satunnainen sijanti
        self.position_apple_height = annetaan omenan pituudelle satunnainen sijainti
        self.positions = annetaan omenalle satunnainen sijainti
        """

    def __init__(self, width, height):
        """Luokan konstruktori"""
        self.width = width
        self.height = height
        self.position_apple_width = random.randint(60, self.width)
        self.position_apple_height = random.randint(60, self.height)
        self.positions = [
            [self.position_apple_width, self.position_apple_height]]

    def new_random_position(self):
        """Palauttaa madolle satunnaisen sijainnin pelilaudalla"""
        self.position_apple_width = random.randint(60, self.width)
        self.position_apple_height = random.randint(60, self.height)
        self.positions = [self.position_apple_width,
                          self.position_apple_height]
