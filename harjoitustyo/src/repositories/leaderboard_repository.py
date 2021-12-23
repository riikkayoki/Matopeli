
class LeaderBoardRepository:

    def __init__(self, connection):

        self._connection = connection
    
    def find_top10(self):

        cursor = self._connection.cursor()
        file = cursor.execute("""
                    SELECT username, points 
                    FROM Leaderboard
                    ORDER BY points DESC
                    LIMIT 10""").fetchall()
        cursor.close()
        return file

    def create_new_highscore(self, username, points):

        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO Leaderboard (username, points) VALUES (?, ?);", [username, points])
        cursor.close()

   
  

   

   