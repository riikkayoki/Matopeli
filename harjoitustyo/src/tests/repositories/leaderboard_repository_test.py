import unittest
from repositories.leaderboard_repository import LeaderBoardRepository
from initialize_database import fake_initialize_database
from database_connection import fake_get_database_connection

class TestLeaderboardRepository(unittest.TestCase):
    def setUp(self):
        fake_initialize_database()
        self.database = LeaderBoardRepository(fake_get_database_connection())
    

    def test_create_new_user_and_find_top10(self):
        self.database.create_new_highscore('riikka', 12)
        self.database.create_new_highscore('riksu', 10)
        self.database.create_new_highscore('erika', 9)
        self.database.create_new_highscore('hello', 8)
        self.database.create_new_highscore('thebest', 7)
        self.database.create_new_highscore('snake94', 6)
        self.database.create_new_highscore('gamer14', 5)
        self.database.create_new_highscore('riksuraksupoksu', 4)
        self.database.create_new_highscore('erkki92', 3)
        self.database.create_new_highscore('hobbit', 0)
   
        top10 = self.database.find_top10()
        self.assertEqual(top10, [('riikka', 12), ('riksu', 10), ('erika', 9), 
                                ('hello', 8), ('thebest', 7), ('snake94', 6), 
                                ('gamer14', 5), ('riksuraksupoksu', 4), ('erkki92', 3), ('hobbit', 0)])