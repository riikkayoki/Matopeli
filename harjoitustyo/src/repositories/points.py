class Points:
    def __init__(self):
        self.points = 0

    def get_point(self, snake_position_x, snake_position_y,
                  apple_position_x, apple_position_y):
        if abs(snake_position_x - apple_position_y) <= 20 and \
                abs(snake_position_y - apple_position_x) <= 20:
            return True
        return False
