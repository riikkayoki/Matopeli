
class LeaderBoardRepository:

    """ A class that tha
    "A class to save the scores of each game in a database.

    Attributes:
            self.connetion: A database connection using sqlite3
    """

    def __init__(self, connection):
        """A constructor of the class that connects the program to the database."""

        self._connection = connection

    def find_top10(self):
        """A method that finds the top 10 best players for the leaderboard."""

        cursor = self._connection.cursor()
        file = cursor.execute("""
                    SELECT username, points 
                    FROM Leaderboard
                    ORDER BY points DESC
                    LIMIT 10""").fetchall()
        cursor.close()
        return file

    def create_new_highscore(self, username, points):
        """A method that creates a new user to the leaderboard database."""

        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO Leaderboard (username, points) VALUES (?, ?);", [
                       username, points])
        cursor.close()
