import sys
import pygame
from entities.snake import Snake
from entities.apple import Apple
from ui.game_ui import GameUI
from ui.form_ui import FormUI
from ui.instructions_menu_ui import InstructionsUI
from ui.leaderboard_menu_ui import LeaderboardMenuUI
from ui.main_menu_ui import MainMenuUI
from ui.renderer import Renderer
from services.points import Points
from repositories.leaderboard_repository import LeaderBoardRepository
from initialize_database import get_database_connection


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.snake = Snake(570, 570)
        self.apple = Apple(570, 570)
        self.points = Points()
        self.game = GameUI()
        self.menu = MainMenuUI()
        self.instructions = InstructionsUI()
        self.leaderboard = LeaderboardMenuUI()
        self.form = FormUI()
        self.database = LeaderBoardRepository(get_database_connection())
        self.display = Renderer(600, 600, (0, 0, 0))

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

    def stop(self):
        if self.snake.game_over():
            pygame.time.delay(500)
            self.stop_game = True
            self.start_game = False
            self.pause = True

    def start(self):
        while True:
            if self.events() is False:
                break
            elif self.start_game:
                self.game.run_game()
                pygame.time.clock(200)
            elif self.stop_game:
                self.form.form()
                if self.enter:
                    self.pause = False
                    self.start_game = False
                    self.database.create_new_highscore(self.form.user_text, 
                                                    self.points.points)
                    self.snake.reset_snake()
                    self.apple.reset_apple()
                    self.points.reset_points()
                    self.stop_game = False
                    self.open_leaderboard = True

            elif self.open_instructions:
                self.instructions.run_instructions_menu()

                if self.go_back:
                    self.open_instructions = False
 
            elif self.open_leaderboard:
                self.leaderboard.run_leaderboard_menu()
                
                if self.go_back:
                    self.open_leaderboard = False
 
            else:
                self.menu.run_main_menu()

            self.go_back = False
            self.enter = False
            self.writing = False
