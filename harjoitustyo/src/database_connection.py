
import sqlite3


def get_database_connection():

    connection = sqlite3.connect("leaderboard.db")
    connection.isolation_level = None

    return connection


def fake_get_database_connection():
    connection = sqlite3.connect("fake_leaderboard.db")
    connection.isolation_level = None

    return connection
