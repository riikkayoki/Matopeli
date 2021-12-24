
import sys
import pygame
from entities.snake import Snake
from entities.apple import Apple
from ui.game_ui import GameUI
from ui.form_ui import FormUI
from ui.instructions_menu_ui import InstructionsMenu
from ui.leaderboard_menu_ui import LeaderboardMenu
from ui.main_menu_ui import MainMenu
from ui.renderer import Renderer
from services.points import Points
from services.gameboard import GameBoard
from repositories.leaderboard_repository import LeaderBoardRepository
from initialize_database import get_database_connection
from services.clock import Clock


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.snake = Snake(570, 570)
        self.apple = Apple(570, 570)
        self.points = Points()
        self.game = GameUI()
        self.game_board = GameBoard(22, 22, pygame.Rect(0, 0, 600, 600))
        self.menu = MainMenu()
        self.instructions = InstructionsMenu()
        self.leaderboard = LeaderboardMenu()
        self.form = FormUI()
        self.database = LeaderBoardRepository(get_database_connection())
        self.display = Renderer(600, 600, (0, 0, 0))
        self.clock = Clock()

        self.start_game, self.stop_game, self.pause = False, False, False
        self.open_instructions, self.open_leaderboard = False, False
        self.go_back, self.enter = False, False
        self.writing = False
    
    def show_game(self):
        with self.display:
            self.snake.move()
            self.update_points(self.snake.position_snake_width, 
                                self.snake.position_snake_height,
                                self.apple.position_apple_width, 
                                self.apple.position_apple_height)
            self.game_over()
            self.game.draw_game_board(self.game_board)
            self.game.draw_apple(self.apple)
            self.game.draw_snake(self.snake)
            self.game.draw_points(self.points.points)
    
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

        
    def update_points(self, position_snake_width, 
                                position_snake_height,
                                position_apple_width, 
                                position_apple_height):
        if self.points.get_point(position_snake_width, 
                                position_snake_height,
                                position_apple_width, 
                                position_apple_height):
            self.apple.new_random_position()
            self.snake.increase_snake_length()
            self.points.points += 1

    def game_over(self):
        if self.snake.border_collision() or self.snake.snake_collision():
            self.clock.tick(500)
            self.stop_game = True
            self.start_game = False
            self.pause = True
      
    def reset_game(self):
        self.pause = False
        self.start_game = False
        self.database.create_new_highscore(self.form.user_text, 
                                                    self.points.points)
        self.snake.reset_snake()
        self.apple.new_random_position()
        self.points.reset_points()
        self.stop_game = False
        self.open_leaderboard = True


    def run(self):
        while True:
            if self.events() is False:
                break
            elif self.start_game:
                self.show_game()
                self.clock.tick(200)
            elif self.stop_game:
                self.form.show_form()
                if self.enter:
                    self.reset_game()
            elif self.open_instructions:
                self.instructions.show_instructions_menu()
                if self.go_back:
                    self.open_instructions = False
            elif self.open_leaderboard:
                self.leaderboard.show_leaderboard_menu()
                if self.go_back:
                    self.open_leaderboard = False
            else:
                self.menu.show_main_menu()

            self.go_back = False
            self.enter = False
            self.writing = False