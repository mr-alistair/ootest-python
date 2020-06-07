from Marker import Marker

class Player(object):
    
    p_playerid = 0
    p_pieces = [None] * 5


    def __init__(self, x_id):

       self.p_playerid = x_id
       
       self.p_pieces = [Marker(x_id),Marker(x_id),Marker(x_id),Marker(x_id),Marker(x_id)]
       

    def p_get_playerid(self):
        return self.p_playerid

    def p_check_game_status(self):

        x_game_over = True

        for x_counter in range(1,5):
            if self.p_pieces[x_counter].m_get_location() != 120:
                x_game_over = False
            else:
                pass
        return x_game_over
