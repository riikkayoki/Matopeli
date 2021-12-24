class Points:
    """A class that keeps track of points in game."""

    def __init__(self):

        """A constructor that defines the point for game."""

        self.points = 0

    def get_point(self, snake_position_width, snake_position_height,
                  apple_position_width, apple_position_height):

        """A method to define when the player gets a point.
        
        Args:
        
        """

        if abs(snake_position_width - apple_position_height) <= 20 and \
                abs(snake_position_height - apple_position_width) <= 20:
            return True
        return False
        


    def reset_points(self):

        """A method to reset points."""
        
        self.points = 0
    

    
    
