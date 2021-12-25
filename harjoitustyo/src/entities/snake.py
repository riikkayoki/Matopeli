import random


class Snake:
    """A class that represents the snake.

    Attributes:
            self.width: width of the area where the snake can be placed.
            self.height: height of the area where the snake can be placed
            self.position_snake_width: random placement of snake width
            self.position_snake_height: random placement of snake height
            self.body: an array of the snake body
            self.directions: a dictionary of the directions where the snake can turn.
            self.direction: a random choice of direction where the snake can turn.
            self.length: an object which keeps track of the snake length, which is used for testing.
            """

    def __init__(self, width: int, height: int):
        """A constructor of the class that defines where the snake can be placed.
        Args: 
            self.width (int): width of the area where the snake can be placed.
            self.height (int): height of the area where the snake can be placed"""

        self.width = width
        self.height = height
        self.position_snake_width = random.randint(60, self.width)
        self.position_snake_height = random.randint(60, self.height)
        self.body = [[self.position_snake_width, self.position_snake_height]]
        self.directions = {'RIGHT': (0, 1), 'LEFT': (0, -1),
                           'UP': (-1, 0), 'DOWN': (1, 0)}
        self.direction = random.choice(['RIGHT', 'LEFT', 'UP', 'DOWN'])
        self.length = 0

    def turn_snake(self, direction: str):
        """A method that allows the snake to turn.
        Args:
            direction: the direction where the player wants to go."""
        self.direction = direction

    def move_snake(self):
        """A method that allows the snake to move."""

        to_move = self.directions[self.direction]
        self.position_snake_width = self.position_snake_width + to_move[0]
        self.position_snake_height = self.position_snake_height + to_move[1]
        self.body.append([self.position_snake_width + to_move[0],
                          self.position_snake_height + to_move[1]])
        self.body.pop(0)

    def increase_snake_length(self):
        """A method that increased the length of the snake and the size of the self.body
        """

        for _ in range(30):
            self.body.append([self.position_snake_width,
                             self.position_snake_height])
        self.length += 1

    def border_collision(self, snake_width, snake_height):
        """A method that defines when the snake touches the game board edges.
        Args:
            snake_width: position of the snake width on the gameboard
            snake_height:position of the snake height on the gameboard"""

        if snake_width == 570 or snake_width == 0 or \
                snake_height == 570 or snake_height == 0:
            return True
        return False

    def snake_collision(self, body):
        """A method that defines when the snake touches itself.
        Args:
            body: an array of the snake body"""

        if body[0] in body[60:]:
            return True
        return False

    def reset_snake(self):
        """A method that resets the snake."""

        self.body = [[self.position_snake_width, self.position_snake_height]]
        self.position_snake_width = random.randint(60, self.width)
        self.position_snake_height = random.randint(60, self.height)
        self.turn_snake(self.direction)
        self.move_snake()
