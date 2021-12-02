import random


class Snake:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.position_snake_width = random.randint(60, self.width)
        self.position_snake_height = random.randint(60, self.height)
        self.positions = [self.position_snake_width, self.position_snake_height]
        self.body = [[self.position_snake_width, self.position_snake_height]]
        self.directions = {'RIGHT': (0, 1), 'LEFT': (0, -1),
                           'UP': (-1, 0), 'DOWN': (1, 0)}
        self.direction = random.choice(['RIGHT', 'LEFT', 'UP', 'DOWN'])
        self.length = 1

    def turn_snake(self, direction):
        self.direction = direction

    def move(self):
        to_move = self.directions[self.direction]
        self.position_snake_width = self.position_snake_width + to_move[0]
        self.position_snake_height = self.position_snake_height + to_move[1]
        self.body.insert(0, [self.position_snake_width + to_move[0],
                             self.position_snake_height + to_move[1]])
        self.body.pop()

    def increase_snake_length(self):
        self.length += 1
        for _ in range(30):
            self.body.insert(
                0, [self.position_snake_width, self.position_snake_height])

    def border_collision(self):
        if self.position_snake_width == 630 or self.position_snake_width == 60:
            return True
        if self.position_snake_height == 630 or self.position_snake_height == 60:
            return True
        return False

    def snake_collision(self):
        if self.positions[0] and self.positions[1] in self.body[1:]:
            return True
        return False
