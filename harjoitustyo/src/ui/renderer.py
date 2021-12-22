import pygame

class Renderer:
    def __init__(self, display_width, display_height, display_color):

        """Luokan konstruktori"""
        self.display_width = display_width
        self.display_height = display_height
        self.display_color = display_color
        pygame.display.set_mode((self.display_width, display_height))
        self.window = pygame.display.get_surface()
    
    def __enter__(self):

        '''Päivittää näytön taustan'''

        self.window.fill(self.display_color)

    def __exit__(self, exc_type, exc_val, exc_tb):

        '''Päivittää näyttöä'''
        pygame.display.update()