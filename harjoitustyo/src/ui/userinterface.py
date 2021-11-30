import pygame


class UserInterface:
    def __init__(self, display_width, display_height, display_color):
        self.display_width = display_width
        self.display_height = display_height
        self.display_color = display_color
        self.grid_size = 30
        pygame.display.set_mode((self.display_width, display_height))
        self.window = pygame.display.get_surface()

    def __enter__(self):
        self.window.fill(self.display_color)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pygame.display.update()

    def draw_game_board(self, game_board):
        for row in range(2, game_board.board_width):
            for column in range(2, game_board.board_height):
                grid_area = pygame.Rect((row * self.grid_size, column * self.grid_size),
                                        (self.grid_size, self.grid_size))
                pygame.draw.rect(self.window, (250, 250, 250), grid_area)

    def draw_snake(self, snake):  # red
        for position in snake.body:
            pygame.draw.rect(self.window, (250, 100, 200),
                             pygame.Rect(position[1], position[0],
                                         self.grid_size, self.grid_size))

    def draw_food(self, apple):  # green
        for _ in apple.positions:
            pygame.draw.rect(self.window, (10, 250, 100),
                             [apple.position_apple_width, apple.position_apple_height,
                              self.grid_size, self.grid_size])

    def draw_points(self):
        font = pygame.font.SysFont('Times New Roman', 30)
        text = font.render('Points: ', False, (10, 100, 10))
        self.window.blit(text, (670, 60))

    def draw_levels(self):
        font = pygame.font.SysFont('Times New Roman', 30)
        text = font.render('Level: ', False, (10, 100, 20))
        self.window.blit(text, (670, 165))

    def draw_game_over(self):
        pass
