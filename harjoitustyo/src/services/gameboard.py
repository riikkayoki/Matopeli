
class GameBoard:

    '''Luokka, joka kuvaa pelilautaa.

    Attributes:
        self.board_width: Merkkijonoarvo, joka kuvaa pelilaudan leveyttä.
        self.board_height: Merkkijonoarvo, joka kuvaa pelilaudan pituutta.
        self.game_area: Muuttuja, joka kuvaa pelialuetta. 
        self.board: Matriisi, joka kuvaa pelilautaa.
        '''

    def __init__(self, board_width, board_height, game_area):

        '''Luokan konstruktori, joka luo pelilaudan.

        Args:
            self.board_width: Merkkijonoarvo, joka kuvaa pelilaudan leveyttä.
            self.board_height: Merkkijonoarvo, joka kuvaa pelilaudan pituutta.
            self.game_area: Muuttuja, joka kuvaa pelialuetta. 
            self.board: Matriisi, joka kuvaa pelilautaa.
        '''

        self.board_width, self.board_height, self.game_area = board_width, board_height, game_area
        self.board = [[0 for _ in range(self.board_width)]
                      for _ in range(self.board_height)]
