import sys
import pygame
from repositories.gameboard import GameBoard
from repositories.apple import Apple
from repositories.snake import Snake
from ui.userinterface import UserInterface
from repositories.points import Points


class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display = UserInterface(1000, 652, (0, 0, 0))
        self.game_board = GameBoard(30, 30, pygame.Rect(30, 30, 600, 600))
        self.snake = Snake(self.game_board.board_width, self.game_board.board_height)
        self.apple = Apple(self.game_board.board_width, self.game_board.board_height)
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

    def game_over(self): # ei toimi
        if self.snake.positions[0] < 0 or self.snake.positions[0] > self.game_board.board_width:
            sys.exit()
        if self.snake.positions[1] < 0 or self.snake.positions[1] > self.game_board.board_height:
            sys.exit()


    def run(self):
        with self.display:
            self.display.draw_game_board(self.game_board)
            self.snake.move()
            if self.snake.snake_head_position() == self.apple.current_apple_position(): # toimii tällä hetkellä vain jos osuu täydellisesti omenaan
                self.apple.new_random_position()
                self.snake.length += 1
                self.points.points += 1
                print(self.snake.length)
                print(self.points.points)
            self.display.draw_snake(self.snake)
            self.display.draw_food(self.apple)
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
