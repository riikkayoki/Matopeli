import sys
import pygame
from gameboard import GameBoard
from entities.snake import Snake
from entities.apple import Apple
from ui.userinterface import UserInterface
from points import Points
from levels import Levels

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display = UserInterface(1000, 720, (0, 0, 0))
        self.game_board = GameBoard(22, 22, pygame.Rect(0, 0, 600, 600))
        self.snake = Snake(570, 570)
        self.apple = Apple(570, 570)
        self.clock = pygame.time.Clock()
        self.points = Points()
        self.level = Levels()

    def directions(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.snake.turn_snake('LEFT')
                if event.key == pygame.K_RIGHT:
                    self.snake.turn_snake('RIGHT')
                if event.key == pygame.K_DOWN:
                    self.snake.turn_snake('DOWN')
                if event.key == pygame.K_UP:
                    self.snake.turn_snake('UP')

    def new_point(self):
        if self.points.get_point(self.snake.position_snake_width,
                                 self.snake.position_snake_height,
                                 self.apple.position_apple_width,
                                 self.apple.position_apple_height):
            self.apple.new_random_position()
            self.snake.increase_snake_length()
            self.points.points += 1

    def new_level(self):
        if self.points.points <= 2:
            self.level.level = 'EASY'
            self.level.easy_level()

        if self.points.points >= 3 and self.points.points < 5:
            self.level.level = 'MEDIUM'
            self.level.medium_level()

        if self.points.points >= 5 and self.points.points < 6:
            self.level.hard_level()
            self.level.level = 'HARD'

        if self.points.points >= 6:
            self.level.level = 'IMPOSSIBLE'
            self.level.impossible_level()

    def game_over(self):
        if self.snake.border_collision():
            sys.exit()

    def run(self):
        with self.display:
            self.snake.move()
            self.new_point()
            self.game_over()
            self.display.draw_game_board(self.game_board)
            self.display.draw_food(self.apple)
            self.display.draw_snake(self.snake)
            self.display.draw_points(self.points.points)
            self.display.draw_levels(self.level.level)

    def start(self):
        while True:
            if self.directions() is False:
                break
            self.run()
            self.new_level()


if __name__ == "__main__":
    GAME = Game()
    RUN = False
    GAME.start()
