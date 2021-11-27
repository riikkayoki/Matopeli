import pygame


class UserInterface:
    def __init__(self, display_width, display_height, display_color):
        self.display_width = display_width
        self.display_height = display_height
        self.display_color = display_color
        pygame.display.set_mode((display_width, display_height))
        self.window = pygame.display.get_surface()
        self.grid_size = 20
     

    def __enter__(self):
        self.window.fill(self.display_color)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pygame.display.update()

    def draw_game_board(self, game_board):
        for row in range(2, int(game_board.board_width)):
            for column in range(2, int(game_board.board_height)):
                if (row + column) % 2 == 0:
                    grid_area = pygame.Rect((row * self.grid_size, column * self.grid_size),
                                            (self.grid_size, self.grid_size))
                    pygame.draw.rect(self.window, (250, 250, 250), grid_area)
                else:
                    grid_area = pygame.Rect((row * self.grid_size, column * self.grid_size),
                                            (self.grid_size, self.grid_size))
                    pygame.draw.rect(self.window, (200, 200, 200), grid_area)

    def draw_snake(self, snake):  # red
        for i in snake.positions:
            grid_area = pygame.Rect((i[1], i[0]),
                                    (self.grid_size, self.grid_size))
            pygame.draw.rect(self.window, (250, 0, 0), grid_area)
           
                

        


    def draw_food(self, food_position):  # blue
        for i in food_position:
            grid_area = pygame.Rect((i[1], i[0]),
                                    (self.grid_size, self.grid_size))
            pygame.draw.rect(self.window, (100, 100, 200), grid_area)

    def draw_points(self):
        pygame.draw.rect(self.window, (200, 200, 200),
                         pygame.Rect(650, 40, 300, 70))
        font = pygame.font.SysFont('Times New Roman', 30)
        text = font.render('Points: ', False, (10, 100, 20))
        self.window.blit(text, (670, 60))

    def draw_levels(self):
        pygame.draw.rect(self.window, (200, 200, 200),
                         pygame.Rect(650, 150, 300, 70))
        font = pygame.font.SysFont('Times New Roman', 30)
        text = font.render('Level: ', False, (10, 100, 20))
        self.window.blit(text, (670, 165))

    def draw_game_over(self):
        pass
