import pygame
from ui.styling_ui import UIStyle
from ui.renderer import Renderer

class FormUI:
    def __init__(self):

        """Luokan konstruktori"""

        self.display = Renderer(600, 600, (0, 0, 0))
        self.style = UIStyle()
        self.write_rect = pygame.Rect(220, 250, 300, 40)
        self.enter_rect = pygame.Rect(220, 300, 80, 30)
        self.user_text = ''

    def form(self):

        '''Päivittää graafista käyttöliityymää, joka tulee näkyviin, 
        kun pelaaja on sijoittunut top 10 pelaajan joukkoon pisteiden perusteella.'''

        with self.display:
            self.draw_highscore_form(self.user_text)
            self.draw_enter_button()

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
    
    def write(self, mouse):

        '''Määrittää painaako pelaaja tekstinsyöttöruutua hiiripainikkeella

        Args: 
            mouse: hiiripainikkeeen klikkauskohta

        Returns: True, jos pelaaja klikkaa tekstinsyöttöruutua, muussa tapauksessa False'''

        if self.write_rect.collidepoint(mouse):
            return True
        return False
    
    def press_enter(self, mouse):

        '''Määrittää, painaako pelaaja enter-nappulaa hiiripainikkeella''

        Args: 
            mouse: hiiripainikkeeen klikkauskohta

        Returns: True, jos pelaaja klikkaa enter-nappulaa, muussa tapauksessa False'''


        if self.enter_rect.collidepoint(mouse):
            return True
        return False