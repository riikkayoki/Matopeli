from ui.userinterface import UserInterface

class LeaderBoardMenu:

    '''Luokka, joka kuvaa tulostaulu-valikkoa.'''

    def __init__(self):

        '''Luokan konstruktori, joka luo tulostaulu-valikon.'''

        self.display = UserInterface(600, 600, (0, 0, 0))
      
    def show_leaderboard(self):

        '''Päivittää graafista käyttöliittymää'''

        with self.display:
            self.display.draw_back_button()
            self.display.draw_leaderboard()
            self.display.draw_top_10()
        
    
   