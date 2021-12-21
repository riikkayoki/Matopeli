
class Points:

    '''Luokka, jonka avulla määritellään milloin pelaaja saa pisteitä.

    Attributes:
        self.points = päivittää pelaajan pisteitä
    '''

    def __init__(self):

        '''Luokan konstruktori, joka pitää yllä pistemäärää'''

        self.points = 0

    def get_point(self, snake_position_width, snake_position_height,
                  apple_position_width, apple_position_height):

        '''Antaa pelaajalle pisteen, kun mato osuu omenaan.

        Args: 
            snake_position_width: Merkkijonoarvo, joka kuvaa madon pituutta.
            snake_position_height: Merkkijonoarvo, joka kuvaa madon pituutta.
            apple_position_width: Merkkijonoarvo, joka kuvaa omenan pituutta.
            apple_position_height: Merkkijonoarvo, joka kuvaa omenan pituutta.

        Returns: True, jos mato osui omenaan, muussa tapauksessa False'''

        if abs(snake_position_width - apple_position_height) <= 20 and \
                abs(snake_position_height - apple_position_width) <= 20:
            return True
        return False
    
    def reset_points(self):
        self.points = 0

   




