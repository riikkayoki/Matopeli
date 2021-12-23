import random

class Apple:

    def __init__(self, width, height):
    
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


    def reset_apple(self):
        self.new_random_position()
        