import random

class Snake(object):
    def __init__(self):
        self.position = (random.randint(0, 30 - 1) * 20, random.randint(0, 30 - 1) * 20)
        self.positions = [(0,0)]
        self.directions = {'RIGHT': (0, 1), 'LEFT': (0, -1), 'UP': (-1, 0), 'DOWN': (1, 0)}
        self.direction = 'RIGHT'

    def turn_snake(self, direction):
        self.direction = direction

    def move(self):
        to_move = self.directions[self.direction]
        self.position = (self.position[0] + to_move[0], self.position[1] + to_move[1])
        self.positions.append(self.position)

        if self.position in self.positions[0:]:
            self.positions = [(self.position[0] + to_move[0], self.position[1] + to_move[1])]
