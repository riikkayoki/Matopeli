
from styling_ui import UIStyle


class FormUI:
    def __init__(self) -> None:
        self.style = UIStyle()

    def draw_highscore_form(self, user_text):
        self.style.text(60, 'GAME OVER', self.black, (80, 50))
        self.style.text(30, 'Thank you for playing!', self.black, (135, 150))
        self.style.text(25, 'Enter nickname: ', self.black, (30, 250))
        self.style.rect(self.style.white, (220, 250, 300, 40))
        self.style.rect_borders(self.style.black, (220, 250, 300, 40), 4)
        self.style.text(22, user_text, self.style.black, (230, 255))
    
    def draw_enter_button(self):
        self.style.rect(self.style.black, (220, 300, 80, 30))
        self.style.rect_borders(self.style.white, (220, 300, 80, 30), 1)
        self.style.text(20, 'ENTER', self.style.grey, (227, 303))