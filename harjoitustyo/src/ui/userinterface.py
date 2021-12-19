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
        for row in range(game_board.board_width):
            for column in range(game_board.board_height):
                grid_area = pygame.Rect((row * self.grid_size, column * self.grid_size),
                                        (self.grid_size, self.grid_size))
                pygame.draw.rect(self.window, (200, 200, 200), grid_area)

    def draw_snake(self, snake):
        """Piirtää madon"""
        for position in snake.body:
            pygame.draw.rect(self.window, (0, 0, 0),
                             pygame.Rect(position[1], position[0],
                                         self.grid_size, self.grid_size))

    def draw_food(self, apple):
        """Piirtää omenan"""
        for _ in apple.positions:
            pygame.draw.rect(self.window, (200, 0, 0),
                             [apple.position_apple_width, apple.position_apple_height,
                              self.grid_size, self.grid_size])

    def draw_points(self, points):
        """Piirtää pisteet"""
        font = pygame.font.SysFont('Times New Roman', 25)
        text = font.render(f'POINTS: {points}', False, (0, 0, 0))
        self.window.blit(text, (460, 10))

    def draw_menu_text(self):
        """Piirtää 'Main Menu' tekstin päävalikkoon"""
        font = pygame.font.SysFont('Times New Roman', 70)
        text = font.render(f'MAIN MENU', False, (200, 200, 200))
        self.window.blit(text, (self.display_width // 4 - 50, 80))

    def draw_start_button(self):
        """Piirtää 'Start' tekstin päävalikkoon"""
        pygame.draw.rect(self.window, (200, 200, 200),
                         pygame.Rect((self.display_width // 4) + 20, 200, 250, 50))
        font = pygame.font.SysFont('Times New Roman', 40)
        text = font.render(f'START GAME', False, (0, 0, 0))
        self.window.blit(text, (self.display_width // 4 + 20, 200))

    def draw_instruction_button(self):
        """Piirtää 'Instructions' tekstin päävalikkoon"""
        pygame.draw.rect(self.window, (200, 200, 200),
                         pygame.Rect(self.display_width // 4 - 2, 400, 290, 50))
        font = pygame.font.SysFont('Times New Roman', 40)
        text = font.render(f'INSTRUCTIONS', False, (0, 0, 0))
        self.window.blit(text, (self.display_width // 4 - 2, 400))

    def draw_leaderboard_button(self):
        pygame.draw.rect(self.window, (200, 200, 200),
                         pygame.Rect(self.display_width // 4 - 5, 300, 300, 50))
        font = pygame.font.SysFont('Times New Roman', 40)
        text = font.render(f'LEADERBOARD', False, (0, 0, 0))
        self.window.blit(text, (self.display_width // 4 - 5, 300))


    def draw_back_button(self):
        """Piirtää 'Back' tekstin käyttöohjevalikkoon"""
        pygame.draw.rect(self.window, (200, 200, 200), pygame.Rect(440, 560, 149, 26))
        font = pygame.font.SysFont('Times New Roman', 20)
        text = font.render(f'BACK TO MENU', False, (0, 0, 0))
        self.window.blit(text, (440, 560))

    def draw_instructions(self):
        """Piirtää käyttöohjeet"""
        font = pygame.font.SysFont('Times New Roman', 25)
        text = font.render('Eat the apples, but do not hit the walls or your own tail!',
                           False, (200, 200, 200))
        self.window.blit(text, (20, 250))

    def draw_form(self):
        """Piirtää tällä hetkellä 'Game over' tekstin"""
        font1 = pygame.font.SysFont('Times New Roman', 60)
        over = font1.render('GAME OVER', False, (0, 0, 0))
        self.window.blit(over, (100, 50))
        font2 = pygame.font.SysFont('Times New Roman', 30)
        thanks = font2.render('Thank you for playing!', False, (0, 0, 0))
        self.window.blit(thanks, (135, 150))
        

    def draw_input_box(self):
        font = pygame.font.SysFont('Times New Roman', 25)
        nickname = font.render('Enter nickname: ', False, (0, 0, 0))
        self.window.blit(nickname, (30, 250))
        pygame.draw.rect(self.window, (250, 250, 250), pygame.Rect(220, 250, 300, 40))
        pygame.draw.rect(self.window, (0, 0, 0), pygame.Rect(220, 250, 300, 40), 5)

    def draw_enter_button(self):
        pygame.draw.rect(self.window, (0, 0, 0), pygame.Rect(220, 300, 80, 30))
        pygame.draw.rect(self.window, (250, 250, 250), pygame.Rect(220, 300, 80, 30), 1)
        font = pygame.font.SysFont('Times New Roman', 20)
        text = font.render(f'ENTER', False, (200, 200, 200))
        self.window.blit(text, (227, 303))
        
    def draw_leaderboard(self):
        font = pygame.font.SysFont('Times New Roman', 20)
        text = font.render(f'LEADERBOARD',
                           False, (200, 200, 200))
        self.window.blit(text, (10, 10))

