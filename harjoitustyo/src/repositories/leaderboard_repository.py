from  database_connection import get_database_connection

class LeaderBoardRepository:
    """Pelisijoituksiin liittyvistä tietokantaoperaatioista vastaava luokka.
        """
    def __init__(self, file_path):
        """Luokan konstruktori.

        Args:
            file_path: Polku tiedostoon, johon tehtävät tallennetaan.
        """
        self._file_path = file_path


    def create(self):
        """Tallentaa sijoituksen nimimerkin ja pisteet tietokantaan"""
        pass

leaderboard_repository = LeaderBoardRepository(get_database_connection())


