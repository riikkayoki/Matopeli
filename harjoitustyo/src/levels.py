import pygame

class Levels:
    def __init__(self):
        self.level = ''
        self.clock = pygame.time.Clock()

    def easy_level(self):
        self.clock.tick(100)

    def medium_level(self):
        self.clock.tick(150)

    def hard_level(self):
        self.clock.tick(200)

    def impossible_level(self):
        self.clock.tick(300)
