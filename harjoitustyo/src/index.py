import sys
import pygame
from services.gameboard import GameBoard
from entities.snake import Snake
from entities.apple import Apple
from ui.userinterface import UserInterface
from services.points import Points
from services.main_menu import MainMenu
from services.form import Form
from services.instructions_menu import InstructionsMenu
from services.leaderboard_menu import LeaderBoardMenu
from repositories.leaderboard_repository import LeaderBoardRepository
from initialize_database import get_database_connection

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display = UserInterface(600, 600, (0, 0, 0))
        self.game_board = GameBoard(22, 22, pygame.Rect(0, 0, 600, 600))
        self.snake = Snake(570, 570)
        self.apple = Apple(570, 570)
        self.points = Points()
        self.menu = MainMenu()
        self.form = Form()
        self.instructions = InstructionsMenu()
        self.leaderboard = LeaderBoardMenu()
        self.database = LeaderBoardRepository(get_database_connection())
        self.start_game, self.stop_game, self.pause = False, False, False
        self.open_instructions, self.open_leaderboard = False, False
        self.go_back, self.enter = False, False
        self.writing = False
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed():
                    if self.menu.to_start(pygame.mouse.get_pos()):
                        self.start_game = True
                    if self.menu.to_instructions(pygame.mouse.get_pos()):
                        self.open_instructions = True
                    if self.menu.to_leaderboard(pygame.mouse.get_pos()):
                        self.open_leaderboard = True
                    if self.menu.back(pygame.mouse.get_pos()):
                        self.go_back = True
                    if self.form.write(pygame.mouse.get_pos()):
                        self.writing = True
                    
                    if self.form.press_enter(pygame.mouse.get_pos()):
                        self.enter = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.snake.turn_snake('LEFT')
                if event.key == pygame.K_RIGHT:
                    self.snake.turn_snake('RIGHT')
                if event.key == pygame.K_DOWN:
                    self.snake.turn_snake('DOWN')
                if event.key == pygame.K_UP:
                    self.snake.turn_snake('UP')

                
                if event.key == pygame.K_BACKSPACE:
                    self.form.user_text = self.form.user_text[:-1]
                else:
                    self.form.user_text += event.unicode
 
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
            pygame.time.delay(500)
            self.stop_game = True
            self.start_game = False
            self.pause = True
        if self.snake.snake_collision():
            pygame.time.delay(500)
            self.stop_game = True
            self.start_game = False
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
            self.display.draw_apple(self.apple)
            self.display.draw_snake(self.snake)
            self.display.draw_points(self.points.points)

    def end_game(self):
        self.pause = False
        self.start_game = False
        self.reset_game()
        self.stop_game = False
 
    def start(self):
        while True:
            if self.events() is False:
                break
            elif self.start_game:
                self.run()
                self.snake.snake_speed(200)
            elif self.stop_game:
                self.form.form()
                if self.enter:
                    self.database._create_new_highscore(self.form.user_text, self.points.points)
                    print(self.database._find_top10())
                    self.end_game()
                    self.open_leaderboard = True
 
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
            self.enter = False
            self.writing = False
         

 
 
if __name__ == "__main__":
    GAME = Game()
    GAME.start()