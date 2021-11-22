import pygame, itertools, pygame.draw

class Food(object):
    def __init__(self):
        self.positions = [(100, 100)]

    def __iter__(self):
        return iter(self.positions)

class Snake(object):
    def __init__(self):
        self.length = 1
        self.positions = [(40, 40)]
        self.up = (0, -1)
        self.down = (0, 1)
        self.left = (-1, 0)
        self.right = (1, 0)
        self.directions = [self.up, self.down, self.left, self.right]

    def __iter__(self):
        return iter(self.positions)

    def turn_snake(self, direction):
        return direction


class GameBoard:
    def __init__(self, board_width, board_height, game_area):
        self.board_width, self.board_height, self.game_area = board_width, board_height, game_area

    def __iter__(self):
        return itertools.product(range(self.board_width), range(self.board_height))

class Main:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display = UserInterface(1000, 652, (0, 0, 0))
        self.game_board = GameBoard(30, 30, pygame.Rect(30, 30, 600, 600))
        self.snake = Snake()
        self.food = Food()

    def directions(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_LEFT:
                    self.snake.turn_snake(self.snake.left)
                if event.type == pygame.K_RIGHT:
                    self.snake.turn_snake(self.snake.right)
                if event.type == pygame.K_DOWN:
                    self.snake.turn_snake(self.snake.down)
                if event.type == pygame.K_UP:
                    self.snake.turn_snake(self.snake.up)
        return True

    def run(self):
        with self.display:
            self.display.draw_game_board(self.game_board)
            self.display.draw_snake(self.snake)
            self.display.draw_food(self.food)
            self.display.draw_points()
            self.display.draw_levels()
        return self.directions()

class UserInterface:
    def __init__(self, display_width, display_height, display_color):
        self.display_width, self.display_height, self.display_color = display_width, display_height, display_color
        pygame.display.set_mode((display_width, display_height))
        self.window = pygame.display.get_surface()
        self.grid_size = 20

    def __enter__(self):
        self.window.fill(self.display_color)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pygame.display.update()

    def draw_game_board(self, game_board):
        for x in range(2, int(game_board.board_width)):
            for y in range(2, int(game_board.board_height)):
                if (x + y) % 2 == 0:
                    grid_area = pygame.Rect((x * self.grid_size, y * self.grid_size), (self.grid_size, self.grid_size))
                    pygame.draw.rect(self.window, (250, 250, 250), grid_area)
                else:
                    grid_area = pygame.Rect((x * self.grid_size, y * self.grid_size), (self.grid_size, self.grid_size))
                    pygame.draw.rect(self.window, (200, 200, 200), grid_area)

    def draw_snake(self, snake_position): # red
        for i in snake_position:
            grid_area = pygame.Rect((i[1], i[0]), (self.grid_size, self.grid_size))
            pygame.draw.rect(self.window, (250, 0, 0), grid_area)

    def draw_food(self, food_position): # blue
        for i in food_position:
            grid_area = pygame.Rect((i[1], i[0]), (self.grid_size, self.grid_size))
            pygame.draw.rect(self.window, (100, 100, 200), grid_area)

    def draw_points(self):
        pygame.draw.rect(self.window, (200, 200, 200), pygame.Rect(650, 40, 300, 70))
        font = pygame.font.SysFont('Times New Roman', 30)
        text = font.render('Points: ', False, (10,100,20))
        self.window.blit(text, (670, 60))

    def draw_levels(self):
        pygame.draw.rect(self.window, (200, 200, 200), pygame.Rect(650, 150, 300, 70))
        font = pygame.font.SysFont('Times New Roman', 30)
        text = font.render('Level: ', False, (10,100,20))
        self.window.blit(text, (670, 165))

if __name__ == "__main__":
    g = Main()
    run = False
    while g.run():
        pygame.display.update()
