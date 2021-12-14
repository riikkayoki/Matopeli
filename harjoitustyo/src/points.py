class Points:
    """Luokka, jonka avulla määritellään milloin pelaaja saa pisteitä"""
    def __init__(self):
        """Luokan konstruktori"""
        self.points = 0

    def get_point(self, snake_position_width, snake_position_height,
                  apple_position_width, apple_position_height):
        if abs(snake_position_width - apple_position_height) <= 20 and \
                abs(snake_position_height - apple_position_width) <= 20:
            return True
        return False

