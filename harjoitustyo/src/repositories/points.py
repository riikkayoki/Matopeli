
from apple import Apple
from snake import Snake


class Points:
    def __init__(self):
        self.points = 0
        self.snake = Snake()
        self.apple = Apple()
        

    def get_point(self):
        if (self.snake.position_x - self.apple.position_x) <= 15 and (self.snake.position_y - self.apple.position_y) <= 15:
            return True
        else:
            return False
