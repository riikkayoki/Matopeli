import pygame


class Clock:
    """A class that represents the pygame clock used in the game."""

    def __init__(self):
        """A class constructor that initializes the pygame clock."""

        self.clock = pygame.time.Clock()

    def tick(self, time):
        """A method that makes the clock to tick.

        Args:
            time: frames per second time."""
        self.clock.tick(time)
