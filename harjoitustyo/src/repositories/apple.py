import random


class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.position_x = random.randint(60, self.x) 
        self.position_y = random.randint(60, self.y)
        self.positions = [[self.position_x, self.position_y]]
        
    def new_random_position(self):
        self.position_x = random.randint(60, self.x) 
        self.position_y = random.randint(60, self.y)
        self.positions = [self.position_x, self.position_y]