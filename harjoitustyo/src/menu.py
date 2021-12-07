import pygame
from ui.userinterface import UserInterface


class Menu:
    def __init__(self):
        self.display = UserInterface(1000, 720, (0, 0, 0))
        self.start_rect = pygame.Rect((self.display.display_width // 3) + 25, 250, 250, 50)
        self.instruction_rect = pygame.Rect(self.display.display_width // 3, 350, 300, 50)
        self.mouse = pygame.mouse.get_pos()

    def start(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_rect.collidepoint(self.mouse):
                    if pygame.mouse.get_pressed():
                        return True
                    else:
                        return False

    def instructions(self):
        if self.instruction_rect.collidepoint(self.mouse):
            if pygame.mouse.get_pressed():
                return True
            else:
                return False
