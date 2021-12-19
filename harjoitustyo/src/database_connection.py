import sqlite3

database = sqlite3.connect("leaderboard.db")
database.isolation_level = None


def get_database_connection():
    return database
