import pygame

class Levels:
    def __init__(self):
        self.level_name = ''
        self.clock = pygame.time.Clock()

    def level(self, number):
        self.clock.tick(number)

