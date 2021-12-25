from ui.styling_ui import UIStyle
from services.renderer import Renderer


class InstructionsMenu:
    """A class that represents the instruction menu.

    Attributes:
            self.display: an object that renders the screen.
            self.style: an object that imports the styling features."""

    def __init__(self):
        """A constructor of the class that initializes the instructions userinterface."""

        self.display = Renderer(600, 600, (0, 0, 0))
        self.style = UIStyle()

    def show_instructions_menu(self):
        """A method that brings the objects to the display."""

        with self.display:
            self.draw_back_button()
            self.draw_instructions()

    def draw_instructions(self):
        """A method to draw the instruction texts."""

        self.style.text(30, 'GAME INSTRUCTIONS', self.style.grey, (130, 25))
        self.style.text(23, '1. Eat the apples, but do not hit the walls or your own tail!',
                        self.style.grey, (20, 100))
        self.style.text(23, '2. Turn the snake with the arrows on your keyboard: ',
                        self.style.grey, (20, 170))
        self.style.text(21, 'Turn right:  Press → on your keyboard',
                        self.style.grey, (50, 220))
        self.style.text(21, 'Turn left:  Press ← on your keyboard',
                        self.style.grey, (50, 260))
        self.style.text(21, 'Turn up:  Press ↑ on your keyboard',
                        self.style.grey, (50, 300))
        self.style.text(21, 'Turn down:  Press ↓ on your keyboard',
                        self.style.grey, (50, 340))
        self.style.text(23, '3. Try to get as much points as possible by eating the apples!',
                        self.style.grey, (20, 400))

    def draw_back_button(self):
        """A method to draw the back to menu -button."""

        self.style.button(self.style.grey, (426, 550, 155, 30), self.style.white,
                          2, 20, 'BACK TO MENU',
                          self.style.black, (430, 553))
