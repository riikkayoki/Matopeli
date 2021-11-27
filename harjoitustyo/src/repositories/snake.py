import random
import pygame
import sys


class Snake:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid_size = 20
        self.random_position = (random.randint(1, self.width) * self.grid_size, random.randint(1, self.height) * self.grid_size)
        self.positions = [(0, 0)]
        self.directions = {'RIGHT': (0, 1), 'LEFT': (0, -1), 'UP': (-1, 0), 'DOWN': (1, 0)}
        self.direction = 'RIGHT'
        
        self.length = 1
    
    def snake_head_position(self):
        return self.positions
        
    def turn_snake(self, direction):
        self.direction = direction

    def move(self):
        to_move = self.directions[self.direction]
        self.random_position = (self.random_position[0] + to_move[0], self.random_position[1] + to_move[1])
        self.positions.append(self.random_position)

        if self.random_position in self.positions[0:]:
            self.positions = [(self.random_position[0] + to_move[0], self.random_position[1] + to_move[1])]

 

