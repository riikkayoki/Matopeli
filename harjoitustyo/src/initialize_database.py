from database_connection import get_database_connection


def drop_table(connection):
    cursor = connection.cursor()
    cursor.execute('''DROP TABLE IF EXISTS Leaderboard;''')
    connection.commit()

def create_table(connection):
    '''Luo tietokantataulun.
    Args:
        connection: Tietokantayhteyden Connection-olio
    '''

    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE Leaderboard (username TEXT, points INTEGER);
    ''')

    connection.commit()

def initialize_database():
    
    '''Alustaa tietokantataulun.'''

    connection = get_database_connection()
    drop_table(connection)
    create_table(connection)


if __name__ == '__main__':
    initialize_database()