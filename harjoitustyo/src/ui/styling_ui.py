import pygame

class UIStyle:
    def __init__(self) -> None:
        self.grey = (200, 200, 200)
        self.black = (0, 0, 0)
        self.white = (250, 250, 250)
        self.red = (200, 0, 0)
        self.window = pygame.display.get_surface()

    def text(self, font_size, text, color, location):
        font = pygame.font.SysFont('Times New Roman', font_size)
        text = font.render(text, False, color)
        self.window.blit(text, location)
    
    def rect(self, color, area):
        pygame.draw.rect(self.window, color, pygame.Rect(area))
    
    def rect_borders(self, color, area, size):
        pygame.draw.rect(self.window, color, pygame.Rect(area), size)
    
    def button(self, rect_color, area, border_color, line, text_size, text, text_color, text_location):
        self.rect(rect_color, area)
        self.rect_borders(border_color, area, line)
        self.text(text_size, text, text_color, text_location)