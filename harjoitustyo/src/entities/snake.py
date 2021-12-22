import random
import pygame


class Snake:
    """Luokka joka kuvaa matoa

    Attributes:
        self.width = madon yhden ruudun leveys
        self.height = madon yhden ruudun pituus
        self.direction = annetaan madolle satunnainen suunta
        self.length = madon pituus
        """
    def __init__(self, width, height):
        """Luokan konstruktori"""
        self.width = width
        self.height = height
        self.position_snake_width = random.randint(60, self.width)
        self.position_snake_height = random.randint(60, self.height)
        self.body = [[self.position_snake_width, self.position_snake_height]]
        self.directions = {'RIGHT': (0, 1), 'LEFT': (0, -1),
                           'UP': (-1, 0), 'DOWN': (1, 0)}
        self.direction = random.choice(['RIGHT', 'LEFT', 'UP', 'DOWN'])
        self.clock = pygame.time.Clock()

    def turn_snake(self, direction):
        """Auttaa matoa kääntymään"""
        self.direction = direction

    def move(self):
        """Auttaa matoa liikkumaan"""
        to_move = self.directions[self.direction]
        self.position_snake_width = self.position_snake_width + to_move[0]
        self.position_snake_height = self.position_snake_height + to_move[1]
        self.body.append([self.position_snake_width + to_move[0],
                          self.position_snake_height + to_move[1]])
        self.body.pop(0)

    def snake_speed(self, speed):
        """Antaa madolle nopeuden"""
        self.clock.tick(speed)

    def increase_snake_length(self):
        """Lisää madon pituutta"""
        for _ in range(30):
            self.body.append([self.position_snake_width, self.position_snake_height])

    def border_collision(self):
        """Tarkistaa osuuko pelilaudan reunaan.

        Returns: True, jos mato osuu pelilaudan reunaan, muussa tapauksessa False"""
        if self.position_snake_width == 570 or self.position_snake_width == 0:
            return True
        if self.position_snake_height == 570 or self.position_snake_height == 0:
            return True
        return False

    def snake_collision(self):
        """Tarkistaa osuuko mato itseensä

        Returns: True, jos mato osuu itseensä, muussa tapauksessa False"""
        if self.body[0] in self.body[60:]:
            return True
        return False

    def reset_snake(self):
        self.body = [[self.position_snake_width, self.position_snake_height]]
        self.position_snake_width = random.randint(60, self.width)
        self.position_snake_height = random.randint(60, self.height)
        self.turn_snake(self.direction)
        self.move()

    def game_over(self):
        if self.border_collision() or self.snake_collision():
            return True
      
        return False
        