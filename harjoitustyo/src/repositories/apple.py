import random


class Apple:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.food_position = [(random.randint(1, self.width) * 20, random.randint(1, self.height) * 20)]
        self.new_random_position()
    
    def __iter__(self):
        return iter(self.food_position)

    def current_apple_position(self):
        return self.food_position
    
    def new_random_position(self):
        self.food_position = [(random.randint(0, 30 - 1) * 20, random.randint(0, 30 - 1) * 20)]
    
  
