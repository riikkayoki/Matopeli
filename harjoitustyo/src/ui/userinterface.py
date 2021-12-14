import pygame

class UserInterface:

    """Luokka joka luo graafisen käyttäliittymän"""
    def __init__(self, display_width, display_height, display_color):
        """Luokan konstruktori"""
        self.display_width = display_width
        self.display_height = display_height
        self.display_color = display_color
        self.grid_size = 30
        pygame.display.set_mode((self.display_width, display_height))
        self.window = pygame.display.get_surface()

    def __enter__(self):
        """Päivittää pelin taustan"""
        self.window.fill(self.display_color)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Päivittää näyttöä"""
        pygame.display.update()

    def draw_game_board(self, game_board):
        """Piirtää pelilaudan"""
        for row in range(2, game_board.board_width):
            for column in range(2, game_board.board_height):
                grid_area = pygame.Rect((row * self.grid_size, column * self.grid_size),
                                        (self.grid_size, self.grid_size))
                pygame.draw.rect(self.window, (250, 250, 250), grid_area)

    def draw_snake(self, snake):
        """Piirtää madon"""
        for position in snake.body:
            pygame.draw.rect(self.window, (250, 100, 200),
                             pygame.Rect(position[1], position[0],
                                         self.grid_size, self.grid_size))
            pygame.draw.rect(self.window, (200, 200, 200),
                             pygame.Rect(position[1], position[0],
                                         self.grid_size, self.grid_size), 1)

    def draw_food(self, apple):
        """Piirtää omenan"""
        for _ in apple.positions:
            pygame.draw.rect(self.window, (10, 250, 100),
                             [apple.position_apple_width, apple.position_apple_height,
                              self.grid_size, self.grid_size])

    def draw_points(self, points):
        """Piirtää pisteet"""
        font = pygame.font.SysFont('Times New Roman', 30)
        text = font.render(f'Points: {points}', False, (200, 200, 200))
        self.window.blit(text, (700, 60))

    def draw_menu_text(self):
        """Piirtää 'Main Menu' tekstin päävalikkoon"""
        font = pygame.font.SysFont('Times New Roman', 70)
        text = font.render(f'MAIN MENU', False, (200, 200, 200))
        self.window.blit(text, ((self.display_width // 3) - 40, 100))

    def draw_start_button(self):
        """Piirtää 'Start' tekstin päävalikkoon"""
        pygame.draw.rect(self.window, (200, 200, 200),
                         pygame.Rect((self.display_width // 3) + 25, 250, 250, 50))
        font = pygame.font.SysFont('Times New Roman', 40)
        text = font.render(f'START GAME', False, (0, 0, 0))
        self.window.blit(text, ((self.display_width // 3) + 25, 250))

    def draw_instruction_button(self):
        """Piirtää 'Instructions' tekstin päävalikkoon"""
        pygame.draw.rect(self.window, (200, 200, 200),
                         pygame.Rect(self.display_width // 3, 350, 300, 50))
        font = pygame.font.SysFont('Times New Roman', 40)
        text = font.render(f'INSTRUCTIONS', False, (0, 0, 0))
        self.window.blit(text, (self.display_width // 3, 350))

    def draw_back_button(self):
        """Piirtää 'Back' tekstin käyttöohjevalikkoon"""
        pygame.draw.rect(self.window, (200, 200, 200), pygame.Rect(900, 600, 80, 30))
        font = pygame.font.SysFont('Times New Roman', 20)
        text = font.render(f'Go Back', False, (0, 0, 0))
        self.window.blit(text, (900, 600))

    def draw_instructions(self):
        """Piirtää käyttöohjeet"""
        font = pygame.font.SysFont('Times New Roman', 40)
        text = font.render(f'Eat the apples, but do not hit the walls or your own tail!',
                           False, (200, 200, 200))
        self.window.blit(text, (60, 300))

    def draw_form(self):
        """Piirtää tällä hetkellä 'Game over' tekstin"""
        font = pygame.font.SysFont('Times New Roman', 40)
        text = font.render('GAME OVER!', False, (200, 200, 200))
        self.window.blit(text, (350, 300))

