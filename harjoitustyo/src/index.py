import sys
import pygame
from repositories.gameboard import GameBoard
from repositories.snake import Snake
from repositories.apple import Apple
from ui.userinterface import UserInterface
from repositories.points import Points


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

    def run(self):
        with self.display:
            self.display.draw_game_board(self.game_board)
            self.snake.move()
            print(self.snake.body)

            if self.points.get_point(self.snake.position_snake_width,
                                     self.snake.position_snake_height,
                                     self.apple.position_apple_width,
                                     self.apple.position_apple_height):
                self.apple.new_random_position()
                self.snake.increase_snake_length()
                self.points.points += 1

            if self.snake.border_collision():
                sys.exit()

            if self.snake.snake_collision():  # ei toimi viel
                sys.exit()

            self.display.draw_food(self.apple)
            self.display.draw_snake(self.snake)
            self.display.draw_points()
            self.display.draw_levels()

    def start(self):
        while True:
            if self.directions() is False:
                break
            self.run()
            self.clock.tick(60)


if __name__ == "__main__":
    GAME = Game()
    RUN = False
    GAME.start()
