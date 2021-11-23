import unittest
from harjoitustyo.src.repositories.snake import Snake

class TestSnake(object):
    def setUp(self):
        self.snake = Snake()


    def test_turn_snake(self, direction):
        s

        # self.direction = direction



    def move(self):
        to_move = self.directions[self.direction]
        self.position = (self.position[0] + to_move[0], self.position[1] + to_move[1])
        self.positions.append(self.position)

        if self.position in self.positions[0:]:
            self.positions = [(self.position[0] + to_move[0], self.position[1] + to_move[1])]
