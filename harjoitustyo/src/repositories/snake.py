import random


class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.position_x = random.randint(60, self.x)
        self.position_y = random.randint(60, self.y)
        self.body = [[self.position_x, self.position_y]]
        self.directions = {'RIGHT': (0, 1), 'LEFT': (0, -1), 'UP': (-1, 0), 'DOWN': (1, 0)}
        self.direction = random.choice(['RIGHT', 'DOWN'])
        
    def turn_snake(self, direction):
        self.direction = direction

    def move(self):
        to_move = self.directions[self.direction] 
        self.position_x = self.position_x + to_move[0]
        self.position_y = self.position_y + to_move[1] 
        self.body.insert(0, [self.position_x + to_move[0], self.position_y + to_move[1]])
        self.body.pop()
      
    def increase_snake_length(self):
        self.body.insert(0, [self.position_x, self.position_y])

    def border_collision(self): 
        if self.position_x == 630 or self.position_x == 60:
            return True
        if self.position_y == 630 or self.position_y == 60:
            return True
        else:
            return False

    def snake_collision(self):
        if (self.position_x in self.body[2:] or self.position_y in self.body[2:]):
            return True
        else:
            return False
        
        

