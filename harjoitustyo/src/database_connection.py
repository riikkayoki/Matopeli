import os
import sqlite3

dirname = os.path.dirname(__file__)


def get_database_connection():
    
    connection = sqlite3.connect(
        os.path.join(dirname, "../..", "data", "leaderboard.db")
        )
    connection.row_factory = sqlite3.Row

    return connection