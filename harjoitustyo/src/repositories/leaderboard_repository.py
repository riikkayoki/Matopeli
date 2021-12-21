
class LeaderBoardRepository:

    '''Tulostauluun liittyvistä tietokantaoperaatioista vastaava luokka.'''
    
    def __init__(self, connection):

        '''Luokan konstruktori.

        Args:
            connection: Polku tiedostoon, johon tehtävät tallennetaan.'''
    
        self._connection = connection
    

    def _find_top10(self):

        '''Palauttaa 10 parasta pelaajaa.
        
        Returns: 
                Palauttaa listan Leaderboard-olioita.'''
        
        cursor = self._connection.cursor()
    
        file = cursor.execute('''SELECT username, points 
                    FROM Leaderboard
                    ORDER BY points
                    LIMIT 10''').fetchall()

        cursor.close()
        return file


    def _create_new_highscore(self, username, points):

        '''Lisää pelaajan tulostauluun. 
        
        Args:
            username: Pelaajan luoma nimimerkki.
            points: Pelaajan saamat pisteet.
        '''

        cursor = self._connection.cursor()
        cursor.execute('INSERT INTO Leaderboard (username, points) VALUES (?, ?);', [username, points])
        cursor.close()
   