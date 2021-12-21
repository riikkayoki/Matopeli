from ui.form_ui import FormUI
import pygame


class Form:

    '''Luokka, joka kuvaa pelin jälkeistä näkymää.

    Attributes:
            self.display: Olio, jolla on UserInterface-luokkaa vastaavat metodit.
            self.write_rect: Kertoo tekstinsyöttöruudun sijainnin.
            self.enter_rect = Kertoo enter-painikkeen sijainnin
            self.user_text = Alustaa merkkijonon tekstin kirjoittamiselle.          
    '''

    def __init__(self):

        '''Luokan konstruktori, joka luo pelin jälkeisen näkymän pelaajalle'''

        self.display = FormUI()
        self.write_rect = pygame.Rect(220, 250, 300, 40)
        self.enter_rect = pygame.Rect(220, 300, 80, 30)
        self.user_text = ''

    def form(self):

        '''Päivittää graafista käyttöliityymää, joka tulee näkyviin, 
        kun pelaaja on sijoittunut top 10 pelaajan joukkoon pisteiden perusteella.'''

        with self.display:
            self.display.draw_highscore_form(self.user_text)
            self.display.draw_enter_button()

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
    




