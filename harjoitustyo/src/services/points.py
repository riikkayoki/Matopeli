class Points:
    """A class that represents the points during the game."""

    def __init__(self):
        """A constructor that initializes the points for the game."""

        self.points = 0

    def get_point(self, snake_width, snake_height,
                  apple_width, apple_height):
        """A method to define when the player gets a point.

        Args:
            snake_width: position of the snake width on the gameboard
            snake_height:position of the snake height on the gameboard
            apple_width: position of the apple width on the gameboard
            snake_height:position of the apple height on the gameboard
        """

        if abs(snake_width - apple_height) <= 20 and \
                abs(snake_height - apple_width) <= 20:
            return True
        return False

    def reset_points(self):
        """A method to reset points."""

        self.points = 0
