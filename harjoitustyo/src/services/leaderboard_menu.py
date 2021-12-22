from ui.leaderboard_menu_ui import LeaderboardMenuUI
class LeaderBoardMenu:

    '''Luokka, joka kuvaa tulostaulu-valikkoa.'''

    def __init__(self):

        '''Luokan konstruktori, joka luo tulostaulu-valikon.'''

        self.display = LeaderboardMenuUI(600, 600, (0, 0, 0))
      
    def show_leaderboard(self):

        '''Päivittää graafista käyttöliittymää'''

        with self.display:
            self.display.draw_back_button()
            self.display.draw_leaderboard_headlines()
            self.display.draw_leaderboard_results()
          
         
        
    
   