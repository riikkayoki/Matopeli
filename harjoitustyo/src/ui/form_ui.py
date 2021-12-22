import pygame
from ui.styling_ui import UIStyle


class FormUI:
    def __init__(self, display_width, display_height, display_color):

        """Luokan konstruktori"""

        self.display_width = display_width
        self.display_height = display_height
        self.display_color = display_color
 
        pygame.display.set_mode((self.display_width, display_height))
        self.window = pygame.display.get_surface()
        self.style = UIStyle()
    
    def __enter__(self):

        '''Päivittää näytön taustan'''

        self.window.fill(self.display_color)

    def __exit__(self, exc_type, exc_val, exc_tb):

        '''Päivittää näyttöä'''
        
        pygame.display.update()

    def draw_highscore_form(self, user_text):
        self.style.text(60, 'GAME OVER', self.style.black, (80, 50))
        self.style.text(30, 'Thank you for playing!', self.style.black, (135, 150))
        self.style.text(25, 'Enter nickname: ', self.style.black, (30, 250))
        self.style.rect(self.style.white, (220, 250, 300, 40))
        self.style.rect_borders(self.style.black, (220, 250, 300, 40), 4)
        self.style.text(22, user_text, self.style.black, (230, 255))
    
    def draw_enter_button(self):
        self.style.rect(self.style.black, (220, 300, 80, 30))
        self.style.rect_borders(self.style.white, (220, 300, 80, 30), 1)
        self.style.text(20, 'ENTER', self.style.grey, (227, 303))