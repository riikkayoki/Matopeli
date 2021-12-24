import sys
import pygame
from ui.styling_ui import UIStyle
from ui.renderer import Renderer
from entities.snake import Snake
from entities.apple import Apple
from ui.form_ui import FormUI
from ui.instructions_menu_ui import InstructionsMenu
from ui.leaderboard_menu_ui import LeaderboardMenu
from ui.main_menu_ui import MainMenu
from ui.renderer import Renderer
from services.points import Points
from services.gameboard import GameBoard
from services.clock import Clock

class GameUI:

    """Luokka joka kuvaa pelin graafista käyttöliittymää."""

    def __init__(self):
        """Luokan konstruktori"""
        self.clock = Clock()
        self.display = Renderer(600, 600, (0, 0, 0))
        self.grid_size = 30
        self.style = UIStyle()
        self.snake = Snake(570, 570)
        self.apple = Apple(570, 570)
        self.points = Points()
        self.game_board = GameBoard(22, 22, pygame.Rect(0, 0, 600, 600))
        self.menu = MainMenu()
        self.instructions = InstructionsMenu()
        self.leaderboard = LeaderboardMenu()
        self.form = FormUI()
        self.display = Renderer(600, 600, (0, 0, 0))
        self.start_game, self.stop_game, self.pause = False, False, False
        self.open_instructions, self.open_leaderboard = False, False
        self.go_back, self.enter = False, False
        self.writing = False

    def show_game(self):
        with self.display:
            self.snake.move() 
            self.draw_game_over()
            self.draw_game_board(self.game_board)
            self.draw_apple(self.apple)
            self.draw_snake(self.snake)
            self.draw_points(self.points.points)

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
                

    def draw_game_board(self, game_board):
        """Piirtää pelilaudan"""

        for row in range(game_board.board_width):
            for column in range(game_board.board_height):
                self.style.rect(self.style.grey,
                                (row * self.grid_size,
                                 column * self.grid_size,
                                 self.grid_size, self.grid_size))

    def draw_snake(self, snake):
        """Piirtää madon"""

        for position in snake.body:
            self.style.rect(self.style.black,
                            (position[1], position[0],
                             self.grid_size, self.grid_size))

    def draw_apple(self, apple):
        """Piirtää omenan"""

        for _ in apple.positions:
            self.style.rect(self.style.red,
                            (apple.position_apple_width,
                             apple.position_apple_height,
                             self.grid_size,
                             self.grid_size))
    
    def draw_points(self, points):
        """Piirtää pisteet"""

        self.style.text(25, f'POINTS: {points}', self.style.black, (460, 10))

  