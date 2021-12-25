import sys
import pygame
from entities.snake import Snake
from entities.apple import Apple
from ui.game_ui import GameUI
from ui.form_ui import FormUI
from ui.instructions_menu_ui import InstructionsMenu
from ui.leaderboard_menu_ui import LeaderboardMenu
from ui.main_menu_ui import MainMenu
from services.renderer import Renderer
from services.points import Points
from services.gameboard import GameBoard
from services.clock import Clock
from repositories.leaderboard_repository import LeaderBoardRepository
from initialize_database import get_database_connection


class Game:
    """A class that represents the game loop that runs the game.

    Attributes:
        self.snake = An object that imports snake methods
        self.apple = An object that imports apple methods
        self.points = An object that imports point methofs
        self.game = An object that imports game userinterface.
        self.game_board = An object that imports the game board.
        self.menu = An object that imports main menu userinterface.
        self.instructions = An object that imports instructions userinterface.
        self.leaderboard = An object that imports leaderboard userinterface.
        self.form = An object that imports the form userinterface.
        self.database = LeaderBoardRepository(get_database_connection())
        self.display = An object that imports rendering methods
        self.clock = An object that imports the clock methods
        self._open_instructions: A boolean value that defines when the intructions menu is open
        self.open_leaderboard: A boolean value that defines when the leaderboard menu is open
        self.go_back: A boolean value that defines when the user goes back to menu.
        """

    def __init__(self):
        """A constructor of the class that initializes the game."""

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
        self._start_game, self._stop_game, self._pause = False, False, False
        self.open_instructions, self.open_leaderboard = False, False
        self.go_back, self._writing, self._enter = False, False, False

    def show_game(self):
        """A method that brings the objects to the display."""

        with self.display:
            self.snake.move_snake()
            self.update_points(self.snake.position_snake_width,
                               self.snake.position_snake_height,
                               self.apple.position_apple_width,
                               self.apple.position_apple_height)
            self.game_over(self.snake.position_snake_width,
                           self.snake.position_snake_height,
                           self.snake.body)
            self.game.draw_game_board(self.game_board)
            self.game.draw_apple(self.apple)
            self.game.draw_snake(self.snake)
            self.game.draw_points(self.points.points)

    def events(self):
        """A method that defines the events for the game."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed():
                    if self.menu.to_start(pygame.mouse.get_pos()):
                        self._start_game = True
                    if self.menu.to_instructions(pygame.mouse.get_pos()):
                        self.open_instructions = True
                    if self.menu.to_leaderboard(pygame.mouse.get_pos()):
                        self.open_leaderboard = True
                    if self.menu.back(pygame.mouse.get_pos()):
                        self.go_back = True
                    if self.form.write(pygame.mouse.get_pos()):
                        self._writing = True
                    if self.form.press_enter(pygame.mouse.get_pos()):
                        self._enter = True

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

    def update_points(self, snake_width, snake_height,
                      apple_width, apple_height):
        """A method to update the points during the game.
        Args:
            snake_width: position of the snake width on the gameboard
            snake_height:position of the snake height on the gameboard
            apple_width: position of the apple width on the gameboard
            snake_height:position of the apple height on the gameboard"""

        if self.points.get_point(snake_width, snake_height,
                                 apple_width, apple_height):

            self.apple.new_random_position()
            self.snake.increase_snake_length()
            self.points.points += 1

    def game_over(self, snake_width, snake_height, body):
        """A method to define when the game is over.
        Args:
            snake_width: position of the snake width on the gameboard
            snake_height: position of the snake height on the gameboard
            body: an array of the snake body"""

        if self.snake.border_collision(snake_width, snake_height) or \
                self.snake.snake_collision(body):
            self.clock.tick(500)
            self._stop_game = True
            self._start_game = False
            self._pause = True

    def reset(self):
        """A method to reset the game for new game."""

        self._pause = False
        self._start_game = False
        self.database.create_new_highscore(self.form.user_text,
                                           self.points.points)
        self.snake.reset_snake()
        self.apple.new_random_position()
        self.points.reset_points()
        self._stop_game = False
        self.open_leaderboard = True

    def run(self):
        """A method to run the game loop."""

        while True:
            if self.events() is False:
                break
            if self._start_game:
                self.show_game()
                self.clock.tick(200)
            elif self._stop_game:
                self.form.show_form()
                if self._enter:
                    self.reset()
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
            self._enter = False
            self._writing = False
