import random


class Apple(object):
    def __init__(self):
        self.food_positions = [(random.randint(0, 30 - 1) * 20, random.randint(0, 30 - 1) * 20)]

    def __iter__(self):
        return iter(self.food_positions)
