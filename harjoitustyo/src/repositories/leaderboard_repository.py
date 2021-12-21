from database_connection import get_database_connection


class LeaderBoardRepository:
    '''Pelisijoituksiin liittyvistä tietokantaoperaatioista vastaava luokka.'''
    
    def __init__(self, connection):
        '''Luokan konstruktori.

        Args:
            connection: Polku tiedostoon, johon tehtävät tallennetaan.
        '''
        self._connection = connection
    

    def _find_top10(self):
        
        cursor = self._connection.cursor()
    
        result = cursor.execute('''SELECT username, points 
                    FROM Leaderboard
                    ORDER BY points
                    LIMIT 10''').fetchall()
        cursor.close()
        return result

    def create_new_highscore(self, username, points):
        cursor = self._connection.cursor()
        cursor.execute('INSERT INTO Leaderboard VALUES (?, ?);', username, points)

    def check_if_highscore(self, points):
        top10 = self._find_top10()
        best_players = len(top10)
        
        if top10[best_players - 1] < points:
                return True
        else:
            return False
