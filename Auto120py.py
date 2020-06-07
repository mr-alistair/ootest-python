
from pip._internal import main
from Game import Game

import pkg_resources.py2_warn

x_gameover = False
x_counter = 1

thisGame = Game()
# SET C is looping or flunking in finding a piece to move... check repeated variables



while not x_gameover:

	x_logstring = "------------------------------------------------------------" + str(x_counter)
	thisGame.g_logmove(x_logstring)

	x_logstring = "Game Move: " + str(x_counter)
	thisGame.g_logmove(x_logstring)
	
	x_playerid = thisGame.g_get_playerturn()
		  
	x_gameover = thisGame.g_player_action(x_playerid)

	for a_counter in range (1,3):
			for b_counter in range (1,5):
				x_outstring = "Player " + str(a_counter) +  " Marker " + str(b_counter) + " Location: " + str(thisGame.g_players[a_counter].p_pieces[b_counter].m_location)
				#print (x_outstring)
				thisGame.g_logmove(x_outstring)
	
	if x_gameover:
		x_clockstop = x_counter
	
	else:
		pass

	x_counter+=1
	
	thisGame.g_flip_player()

for x_counter_output in (thisGame.g_movelog):
	print (x_counter_output)
	pass

print ("\nFINAL MOVE: " + str(x_clockstop) + "\n")
