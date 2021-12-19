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
        self.gray = (200, 200, 200)
        self.black = (0, 0, 0)
        self.white = (250, 250, 250)
        self.red = (200, 0, 0)
        
    def __enter__(self):
        """Päivittää pelin taustan"""
        self.window.fill(self.display_color)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Päivittää näyttöä"""
        pygame.display.update()
    
    def text(self, font_size, text, color, location):
        font = pygame.font.SysFont('Times New Roman', font_size)
        text = font.render(text, False, color)
        self.window.blit(text, location)
    
    def rect(self, color, area):
        pygame.draw.rect(self.window, color, pygame.Rect(area))

    def draw_game_board(self, game_board):
        """Piirtää pelilaudan"""
        for row in range(game_board.board_width):
            for column in range(game_board.board_height):
                self.rect(self.gray, (row * self.grid_size, column * self.grid_size,
                                        self.grid_size, self.grid_size))

    def draw_snake(self, snake):
        """Piirtää madon"""
        for position in snake.body:
            self.rect(self.black, (position[1], position[0],
                                         self.grid_size, self.grid_size))

    def draw_food(self, apple):
        """Piirtää omenan"""
        for _ in apple.positions:
            self.rect(self.red, (apple.position_apple_width, apple.position_apple_height,
                              self.grid_size, self.grid_size))

    def draw_points(self, points):
        """Piirtää pisteet"""
        self.text(25, f'POINTS: {points}', self.black, (460,10))

    def draw_menu_text(self):
        """Piirtää 'Main Menu' tekstin päävalikkoon"""
        self.text(70, 'MAIN MENU', self.gray, (self.display_width // 4 - 50, 80))

    def draw_start_button(self):
        """Piirtää 'Start' tekstin päävalikkoon"""
        self.rect(self.gray, ((self.display_width // 4) + 20, 200, 250, 50))
        self.text(40, 'START GAME', self.black, (self.display_width // 4 + 20, 200))

    def draw_instruction_button(self):
        """Piirtää 'Instructions' tekstin päävalikkoon"""
        self.rect(self.gray, (self.display_width // 4 - 2, 400, 290, 50))
        self.text(40, 'INSTRUCTIONS', self.black, (self.display_width // 4 - 2, 400))

    def draw_leaderboard_button(self):
        self.rect(self.gray, (self.display_width // 4 - 5, 300, 300, 50))
        self.text(40, 'LEADERBOARD', self.black, (self.display_width // 4 - 5, 300))

    def draw_back_button(self):
        """Piirtää 'Back' tekstin käyttöohjevalikkoon"""
        self.rect(self.gray, (440, 560, 149, 26))
        self.text(20, 'BACK TO MENU', self.black, (440, 560))

    def draw_instructions(self):
        """Piirtää käyttöohjeet"""
        self.text(25, 'Eat the apples, but do not hit the walls or your own tail!', self.gray, (20, 250))

    def draw_form_texts(self):
        """Piirtää tällä hetkellä 'Game over' tekstin"""
        self.text(60, 'GAME OVER :-(', self.black, (80, 50))
        self.text(30, 'Thank you for playing!', self.black, (135, 150))
        self.text(25, 'Enter nickname: ', self.black, (30, 250))
        
    def draw_input_box(self):
        self.rect(self.white, (220, 250, 300, 40))
        pygame.draw.rect(self.window, (0, 0, 0), pygame.Rect(220, 250, 300, 40), 5)

    def draw_enter_button(self):
        self.rect(self.black, (220, 300, 80, 30))
        pygame.draw.rect(self.window, (250, 250, 250), pygame.Rect(220, 300, 80, 30), 1)
        self.text(20, 'ENTER', self.gray, (227, 303))
        
    def draw_leaderboard(self):
        self.text(20, 'LEADERBOARD', self.gray, (10, 10))
  
