
from repositories.gameboard import *
from repositories.apple import *
from repositories.snake import *
from ui.userinterface import *


class Main:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display = UserInterface(1000, 652, (0, 0, 0))
        self.game_board = GameBoard(30, 30, pygame.Rect(30, 30, 600, 600))
        self.snake = Snake()
        self.apple = Apple()
        self.clock = pygame.time.Clock()

    def directions(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print('left')
                    self.snake.turn_snake('LEFT')
                if event.key == pygame.K_RIGHT:
                    self.snake.turn_snake('RIGHT')
                if event.key == pygame.K_DOWN:
                    self.snake.turn_snake('DOWN')
                if event.key == pygame.K_UP:
                    self.snake.turn_snake('UP')

    def run(self):
        with self.display:
            self.snake.move()

            self.display.draw_game_board(self.game_board)
            self.display.draw_snake(self.snake)
            self.display.draw_food(self.apple)
            self.display.draw_points()
            self.display.draw_levels()

    def start(self):
        while True:
            if self.directions() == False:
                break
            self.run()
            self.clock.tick(60)


if __name__ == "__main__":
    g = Main()
    run = False
    g.start()
