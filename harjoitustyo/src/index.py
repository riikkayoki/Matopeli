import sys
import pygame
from services.gameboard import GameBoard
from entities.snake import Snake
from entities.apple import Apple
from ui.userinterface import UserInterface
from services.points import Points
from services.main_menu import MainMenu
from form import Form
from services.instructions_menu import InstructionsMenu
from services.leaderboard_menu import LeaderBoardMenu


class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display = UserInterface(600, 600, (0, 0, 0))
        self.game_board = GameBoard(22, 22, pygame.Rect(0, 0, 600, 600))
        self.snake = Snake(570, 570)
        self.apple = Apple(570, 570)
        self.clock = pygame.time.Clock()
        self.points = Points()
        self.menu = MainMenu()
        self.form = Form()
        self.instructions = InstructionsMenu()
        self.leaderboard = LeaderBoardMenu()
        self.start_game = False
        self.go_back = False
        self.stop_game = False
        self.text = ''
        self.enter = False
        self.writing = False
        self.pause = False
        self.open_instructions = False
        self.open_leaderboard = False
    
    def events(self):
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

                if self.writing:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed():
                    if self.menu.start(pygame.mouse.get_pos()):
                        self.start_game = True
                    if self.menu.instructions(pygame.mouse.get_pos()):
                        self.open_instructions = True
                    if self.menu.to_leaderboard(pygame.mouse.get_pos()):
                        self.open_leaderboard = True
                    if self.instructions.back(pygame.mouse.get_pos()):
                        self.go_back = True
                    if self.form.write(pygame.mouse.get_pos()):
                        self.writing = True
                    if self.form.press_enter(pygame.mouse.get_pos()):
                        self.enter = True


            
    def update_points(self):
        if self.points.get_point(self.snake.position_snake_width,
                                 self.snake.position_snake_height,
                                 self.apple.position_apple_width,
                                 self.apple.position_apple_height):
            self.apple.new_random_position()
            self.snake.increase_snake_length()
            self.points.points += 1

    def game_over(self):
        if self.snake.border_collision():
            self.stop_game = True
            pygame.time.delay(500)
            self.pause = True
        if self.snake.snake_collision():
            self.stop_game = True
            pygame.time.delay(500)
            self.pause = True
    
    def reset_game(self):
        self.snake.reset_snake()
        self.apple.reset_apple()
        self.points.reset_points()

    def run(self):
        with self.display:
            self.snake.move()
            self.update_points()
            self.game_over()
            self.display.draw_game_board(self.game_board)
            self.display.draw_food(self.apple)
            self.display.draw_snake(self.snake)
            self.display.draw_points(self.points.points)
         
    def start(self):
        while True:
            if self.events() is False:
                break

            elif self.start_game:
                self.run()
                self.snake.snake_speed(200)
                if self.stop_game:
                    while self.pause:
                        self.form.form()
                        if self.enter:
                            self.pause = False
                            self.start_game = False
                            self.reset_game()

            elif self.open_instructions:
                self.instructions.show_instructions()
                if self.go_back:
                    self.open_instructions = False
            
            elif self.open_leaderboard:
                self.leaderboard.show_leaderboard()
                if self.go_back:
                    self.open_leaderboard = False

            else:
                self.menu.main_menu()
            self.go_back = False
            self.stop_game = False
            self.enter = False
            self.writing = False


if __name__ == "__main__":
    GAME = Game()
    GAME.start()
