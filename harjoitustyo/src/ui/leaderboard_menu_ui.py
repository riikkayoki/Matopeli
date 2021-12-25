from database_connection import get_database_connection
from repositories.leaderboard_repository import LeaderBoardRepository
from ui.styling_ui import UIStyle
from services.renderer import Renderer


class LeaderboardMenu:
    """A class that represents the leaderboard menu.

    Attributes:
            self.database: creates a connection to the database.
            self.display: an object that renders the screen.
            self.style: an object that imports the styling features."""

    def __init__(self):
        """A constructor of the class that initializes the leaderboard userinterface."""

        self.database = LeaderBoardRepository(get_database_connection())
        self.style = UIStyle()
        self.display = Renderer(600, 600, (0, 0, 0))

    def show_leaderboard_menu(self):
        """A method that brings the objects to the display."""

        with self.display:
            self.draw_back_button()
            self.draw_leaderboard_headlines()
            self.draw_leaderboard_results()

    def draw_leaderboard_headlines(self):
        """A method to draw the leaderboard headline texts."""

        self.style.text(30, 'LEADERBOARD', self.style.grey, (180, 25))
        self.style.text(23, 'ranking', self.style.grey, (100, 95))
        self.style.text(23, 'username', self.style.grey, (220, 95))
        self.style.text(23, 'points', self.style.grey, (430, 95))

    def draw_leaderboard_results(self):
        """A method to draw the leaderboard statistics."""

        results = self.database.find_top10()
        count = 0
        heigth = 0

        for highscores in results:
            count += 1
            heigth += 35
            self.style.text(20, f'{count}', self.style.grey,
                            (125, 105 + heigth))
            self.style.text(20, f'{highscores[0]}', self.style.grey,
                            (222, 105 + heigth))
            self.style.text(20, f'{highscores[1]}', self.style.grey,
                            (455, 105 + heigth))

    def draw_back_button(self):
        """A method to draw the back to menu -button."""

        self.style.button(self.style.grey, (426, 550, 155, 30),
                          self.style.white,
                          2, 20, 'BACK TO MENU',
                          self.style.black, (430, 553))
