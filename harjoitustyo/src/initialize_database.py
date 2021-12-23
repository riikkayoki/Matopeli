from database_connection import fake_get_database_connection, get_database_connection


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

    connection = get_database_connection()
    drop_table(connection)
    create_table(connection)

def fake_initialize_database():
    
    connection = fake_get_database_connection()
    drop_table(connection)
    create_table(connection)

if __name__ == '__main__':
    initialize_database()