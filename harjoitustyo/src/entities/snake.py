import random
import pygame


class Snake:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.position_snake_width = random.randint(60, self.width)
        self.position_snake_height = random.randint(60, self.height)
        self.body = [[self.position_snake_width, self.position_snake_height]]
        self.directions = {'RIGHT': (0, 1), 'LEFT': (0, -1),
                           'UP': (-1, 0), 'DOWN': (1, 0)}
        self.direction = random.choice(['RIGHT', 'LEFT', 'UP', 'DOWN'])
        self.length = 1
        self.clock = pygame.time.Clock()

    def turn_snake(self, direction):
        self.direction = direction
        pass

    def move(self):
        to_move = self.directions[self.direction]
        self.position_snake_width = self.position_snake_width + to_move[0]
        self.position_snake_height = self.position_snake_height + to_move[1]
        self.body.append([self.position_snake_width + to_move[0],
                          self.position_snake_height + to_move[1]])
        self.body.pop(0)

    def snake_speed(self, speed):
        self.clock.tick(speed)

    def increase_snake_length(self):
        self.length += 1
        for _ in range(30):
            self.body.append([self.position_snake_width, self.position_snake_height])

    def border_collision(self):
        if self.position_snake_width == 630 or self.position_snake_width == 60:
            return True
        if self.position_snake_height == 630 or self.position_snake_height == 60:
            return True
        return False

    def snake_collision(self):
        if self.body[0] in self.body[60:]:
            return True
        return False
