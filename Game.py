from Player import Player
from Marker import Marker

import random
import datetime

class Game(object):
    
	g_movecounter = 0
	g_movelog = []
	g_playerturn = 0
	g_players = [None] * 3
	g_dievalue = 0
	g_gameover = False

	def __init__(self):

		self.g_newgame()

		self.g_movecounter = 0

		self.g_playerturn = random.randint(1,2)

		x = random.randint

		self.g_logmove( "Player " + str(self.g_playerturn) + " will go first." )

		self.g_dievalue = 0

		self.g_gameover = False


	def g_logmove(self, x_logmove):
		self.g_movecounter+=1
		g_now = datetime.datetime.now()
		g_now_string = g_now.strftime("%Y-%m-%d %H:%M:%S") + " - - " + x_logmove
		self.g_movelog.append(g_now_string)
		#print(g_now_string)


	def g_newgame(self):

		self.g_players[1] = Player(1)
		self.g_players[2] = Player(2)
	

	def g_flip_player(self):
		if self.g_playerturn == 1:
			self.g_playerturn = 2
		else:
			self.g_playerturn = 1


	def g_diceroll(self):
		self.g_dievalue = random.randint(1,6)
		return self.g_dievalue


	def g_return_other_player(self):
		if self.g_get_playerturn() == 1:
			return self.g_players[2]
		else:
			return self.g_players[1]


	def g_return_player(self,x_playerid):
		return self.g_players[x_playerid]

	
	def g_find_to_move_onto_board(self, x_player):
		#temp properties
		x_piece_array_pointer = [0] * 5
		x_logstring = ""      
		x_counter_array = 0
		x_counter = 0



		for x_counter in range (1,5):
			if (x_player.p_pieces[x_counter].m_get_location() == 1):
			   x_counter_array+=1
			   x_piece_array_pointer[x_counter_array] = x_counter
			else:
				pass

		#If there is one or more, return one at random
		if x_counter_array > 0:
			return x_piece_array_pointer[random.randint(1,x_counter_array)]
		else:
    		# there were no markers "off the board" ... return an empty pointer
			x_logstring = "Player " + str(x_player.p_get_playerid()) + " was in SET D but could not find markers to move onto the board..."
			self.g_logmove(x_logstring)
			return 0

	
	def g_find_to_move_in_play(self, x_player):
	
		#temp properties
		x_piece_array_pointer = [0] * 5
		x_piece_array_backup = [0] * 5
		x_logstring = ""
		x_test_1 = False
		x_test_2 = False
		x_counter_array = 0
		x_temp_value = 0

		x_temp_magic_numbers = [20,24,30,40,60]

		#FOR1
		for x_counter_a in range(1,5):

       		#find a player's marker which is active
			if x_player.p_pieces[x_counter_a].m_get_status() == True:
				x_counter_array+=1
				x_piece_array_pointer[x_counter_array] = x_counter_a
				x_piece_array_backup[x_counter_array] = x_counter_a
			else:
				pass
		#ENDFOR 1		

		#BIGIF1
		#If there is one or more, return one at random
		if x_counter_array > 0:
			x_logstring = "Considering between " + str(x_counter_array) + " potential piece(s)."
			self.g_logmove(x_logstring)
			#FOR2
			for x_counter_loop_a in range(1,x_counter_array+1):

				x_test_1 = False		
				x_test_2 = False

				x_temp_value = x_piece_array_pointer[x_counter_loop_a]
		
				x_logstring = "Step " + str(x_counter_loop_a) + " of " + str(x_counter_array) + "..Looking at piece: " + str(x_temp_value) + " at location " + str(x_player.p_pieces[x_temp_value].m_get_location())
	
				self.g_logmove(x_logstring)
		
				x_test_1 = x_temp_value in x_temp_magic_numbers

				if x_test_1:
					x_logstring = "Considering ignoring piece " + str(x_temp_value) + " as it is on a penultimate number."
					self.g_logmove(x_logstring)
				else:
										pass

				if (x_player.p_pieces[x_temp_value].m_get_location() * self.g_dievalue) > 120:
					x_test_2 = True
					x_logstring = "Considering ignoring piece " + str(x_temp_value) + " as it may cause a blowout."
					self.g_logmove(x_logstring)
				else:
					pass

				if x_test_1 or x_test_2:
					x_piece_array_backup[x_counter_loop_a] = 999
				else:
					pass
	
							#ENDFOR2
			########################
			# find the number of pieces in the backup array
			x_counter_b = 0
			#FOR3
			for x_counter_loop_b in range(1,5):
				if (x_piece_array_backup[x_counter_loop_b] != 999) and (x_piece_array_backup[x_counter_loop_b] > 0):
					x_counter_b+=1
				else:
					pass
			#ENDFOR3
			##################################################	

			#pick a pointer at random from the remainder    
			#BIG IF 2
			if x_counter_b == 0:
				x_temp_value = 0
				x_logstring = "Ignored too many...reverting."
				self.g_logmove(x_logstring)
				for x_counter_loop_c in range (1,5):
					if x_piece_array_pointer[x_counter_loop_c] != 999 and x_piece_array_pointer[x_counter_loop_c] > 0:
						x_temp_value+=1
					else:
						pass
				#ENDFOR
				x_logstring = "Player " +str(x_player.p_get_playerid()) + " has " + str(x_temp_value) + " possible piece(s) to move."
				self.g_logmove(x_logstring)
				x_test_1 = True
				while x_test_1:
					x_counter_array = random.randint(1,4)	
					if x_piece_array_pointer[x_counter_array] > 0 and x_piece_array_pointer[x_counter_array] != 999:
						x_test_1 = False # FOUND ONE TO MOVE AND IT IS IN THE ARRAY_POINTER AT POSITION X_COUNTER_ARRAY
					else:
						pass
				#END WHILE
			else:	#BRANCH ELSE
				#pick one from the backup array to use
				x_temp_value = 0
				for x_counter_loop_d in range (1,5): 
					if (x_piece_array_backup[x_counter_loop_d] != 999) and (x_piece_array_backup[x_counter_loop_d] > 0):
						x_temp_value+=1
					else:
						pass
				
				#END FOR
				
				x_logstring = "Choosing one from the remaining markers..." #must choose a random from the remaining 'good' pointers in the live array
				self.g_logmove(x_logstring)
				x_logstring = "Player " + str(x_player.p_get_playerid()) + " has " + str(x_temp_value) + " possible piece(s) to move which are on the board..."
				self.g_logmove(x_logstring)

				x_test_1 = True
				while x_test_1:
					x_counter_array = random.randint(1,4)
					if (x_piece_array_backup[x_counter_array] > 0) and (x_piece_array_backup[x_counter_array] != 999):
						x_test_1 = False #found one to move	
					else:
						pass
				#END WHILE
			#END BIG IF 2

			x_logstring = "Player " + str(x_player.p_get_playerid())  + " has chosen to move piece " + str(x_piece_array_pointer[x_counter_array])
		
			self.g_logmove(x_logstring)

		else:  #BIG IF 1 BRANCH 
				#there were no markers 'on the board'...return an empty pointer;
		#this is captured by the calling function and acted upon        
			return 0
	
		return x_piece_array_pointer[x_counter_array]

	def g_move_onto_board_set_D(self, x_player):
		
		x_piece_pointer = self.g_find_to_move_onto_board(x_player)

		if x_piece_pointer == 0:
			
			#no more pieces to move on to the board
			x_logstring = "Player " + str(x_player.p_get_playerid())  + " did not have pieces to move into play."
			self.g_logmove(x_logstring)
			
			return False

		else:
				self.g_marker_move(x_player.p_get_playerid(), x_piece_pointer)
								
				return True

	def g_marker_move(self, x_playerid, x_piece_pointer):

		x_logstring = ""

		x_text = ""

		x_old_position = 0

		x_new_location = 0
	
		x_other_player = self.g_return_other_player()

		x_old_position = self.g_players[x_playerid].p_pieces[x_piece_pointer].m_get_location()

			
		if self.g_dievalue != 0:
			x_pass_value = self.g_dievalue
			x_new_location = self.g_players[x_playerid].p_pieces[x_piece_pointer].m_calclocation(x_pass_value)
		else:
			#Piece has been bumped to the start either due to clash or blow-out
			x_new_location = 1
	

		if x_new_location > 120:
	
			#blow-out!
			x_logstring = "Player " + str(x_playerid) + " busted piece " + str(x_piece_pointer) + " to a value of " + str(x_new_location) + "!"
			self.g_logmove(x_logstring);
			x_new_location = 1
		else:
			pass
	
	
		self.g_players[x_playerid].p_pieces[x_piece_pointer].m_setlocation(x_new_location)

		x_logstring = "[[[Player " + str(x_playerid)  + " moved piece " + str(x_piece_pointer) + " from position " + str(x_old_position) + " to " + str(self.g_players[x_playerid].p_pieces[x_piece_pointer].m_get_location())  + "]]]"

		self.g_logmove(x_logstring)



		if x_new_location == 120:
			#piece has made it to the end and will be disabled

			if self.g_players[x_playerid].p_pieces[x_piece_pointer].m_get_status():
				x_text = "ACTIVE"
			else:
				x_text = "INACTIVE"

			x_logstring = "Player " + str(x_playerid) + "s piece " + str(x_piece_pointer) + " has reached position " + str(self.g_players[x_playerid].p_pieces[x_piece_pointer].m_get_location())  + " successfully and is now " + x_text

			self.g_logmove(x_logstring)
		else:
			pass

		#call clash detect unless it has moved to 1
		if (x_new_location != 1) and (x_new_location != 120):
				self.g_detect_clash(self.g_players[x_playerid].p_pieces[x_piece_pointer].m_get_location(), x_other_player)
		else:
			pass
	
		
		self.g_gameover = self.g_players[x_playerid].p_check_game_status()



	def g_detect_clash(self, x_location, x_player):
		
		#iterate through opposing players active pieces and reset them if the new move has caused a clash

		x_return_flag = False

		for x_counter in range (1,5):
			#find an (opposition) player's marker which is on the board but active

			if (x_player.p_pieces[x_counter].m_get_location() == x_location and x_player.p_pieces[x_counter].m_get_status()):
				#bump the clash piece
				self.g_dievalue = 0
				self.g_marker_move(x_player.p_get_playerid(), x_counter)
				x_logstring = "Player "  + str(x_player.p_get_playerid()) + "'s piece " + str(x_counter) + " was bumped to the start of the board!"
				self.g_logmove(x_logstring)
				x_return_flag = True
			else:
				#if it doesn't find a clash, do nothing
				pass

		return x_return_flag



	def g_player_action(self, x_playerid):
		
		x_result = False
		x_test = ""
	
		x_temp_magic_numbers = [ 0, 20, 24, 30, 40, 60, 120 ]

		x_temp_factor_numbers = [ 0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 25, 50 ]

		x_logstring = ""

		self.g_dievalue = self.g_diceroll()

		x_logstring = "[[[Player " + str(x_playerid) + " rolled a " + str(self.g_dievalue) + " ]]]"

		self.g_logmove(x_logstring)


		if self.g_dievalue == 1:
				x_logstring = "Player " + str(x_playerid)  + " has to forfeit their move!"
				self.g_logmove(x_logstring)
		else:
				#SET A
				x_result = self.g_target_magic_numbers(x_playerid, x_temp_magic_numbers, "penultimate",6)

				#SET B
				if not x_result:
					x_logstring = "Player " + str(x_playerid) + " did not find any penultimate targets."
					self.g_logmove(x_logstring)
					x_result = self.g_target_magic_numbers(x_playerid, x_temp_factor_numbers, "factor", 12)
				else:
					pass

				
				#SET C
				if not x_result:
					x_logstring = "Player " + str(x_playerid) + " did not find any factor targets."
					self.g_logmove(x_logstring)

					x_result = self.g_target_potential_clashes_set_C(self.g_players[x_playerid])

				else:
					pass

				#SET D
				if not x_result:
					x_result = self.g_move_onto_board_set_D(self.g_players[x_playerid])
					self.g_logmove("SET D result is " + str(x_result))

				else:
					pass

		if (self.g_gameover):
				print("**************************************\n");
				print("***   Player " + str(x_playerid) + " HAS WON THE MATCH! ***\n");
				print("**************************************\n");

				self.g_logmove("************************************");
				x_logstring = "***   Player " + str(x_playerid) + " HAS WON THE MATCH! ***"
				self.g_logmove(x_logstring)

				self.g_logmove("************************************");

		else:
			pass

		return self.g_gameover



	def g_target_magic_numbers(self, x_playerid, x_magicnumbers, x_type, x_magic_count):
		x_forecast_dummy = [0] * 3
		x_forecast_pointers = [x_forecast_dummy] * 5
		x_found_target = False
		x_test_count_flag = False
		x_piece_pointer = 0
		x_counter = 0
		x_counter_m = 0
		x_counter_test = 0
		x_temp_forecast = 0

		#populate current players positions and status to temporary array
		for x_counter_a in range (1,5): 		
			if not self.g_players[x_playerid].p_pieces[x_counter_a].m_get_status():
				#this piece is out of play - set up a dummy which will never get hit
				x_forecast_pointers[x_counter_a][0] = x_counter_a
				x_forecast_pointers[x_counter_a][1] = 999
				x_forecast_pointers[x_counter_a][2] = 0
			else:
				#otherwise, put in a forecast of where it would land based on the dice roll
				x_forecast_pointers[x_counter_a][0] = x_counter_a
				x_forecast_pointers[x_counter_a][1] = self.g_players[x_playerid].p_pieces[x_counter_a].m_get_location() * self.g_dievalue
				x_forecast_pointers[x_counter_a][2] = 0

	
		#now for each potential location see if there is a match in magic numbers
		for x_counter_m in range (1,5): 
			x_temp_forecast = x_forecast_pointers[x_counter_m][1]

			if x_temp_forecast in x_magicnumbers:
				#found one
					x_forecast_pointers[x_counter_m][2] = 1
			else:
				pass

		#clear the array of player's pieces that are not a magic target
		x_test_count_flag = False

		for x_counter_test in range (1,5): 
			if x_forecast_pointers[x_counter_test][2] == 1:
				#found at least one
				x_test_count_flag = True
			else:
				# set the rest to dummy
				x_forecast_pointers[x_counter_test][2] = 999

		#got at least one potential target
		if x_test_count_flag:
			#now we have an array of only the possible markers to select to target
			#loop until we find one that is not 999

			while not x_found_target:
				x_counter_c = random.randint(1,4)
				if x_forecast_pointers[x_counter_c][2] != 999:
					#the piece we choose to move
					x_piece_pointer = x_forecast_pointers[x_counter_c][0]
					x_logstring = "Player " + str(x_playerid) + " is selecting " + x_type + " target at location " + str(x_forecast_pointers[x_counter_c][1]) + " with piece " + str(x_piece_pointer) + "             ***"
					self.g_logmove(x_logstring)
					self.g_marker_move(x_playerid,  x_piece_pointer)
					x_found_target = True
				else:
					pass

		else:
			x_found_target = False

		return x_found_target
	


	def g_target_potential_clashes_set_C(self, x_player):

		#properties
		x_temp_pointer_list = [None] * 5
		x_forecast_pointers = [x_temp_pointer_list] * 5
		x_found_target = False
		x_test_count_flag = False
		x_piece_pointer = 0
		x_temp_branch = 2
		x_counter = 0
		x_counter_o = 0
		x_counter_p = 0
		x_counter_test = 0
		x_temp_opp_location = 0
		x_temp_opp = self.g_return_other_player()
		x_offboard_flag = False
		x_onboard_flag = False

		#populate current players positions and status to temporary array
		for x_counter in range (1,5): 
			if not x_player.p_pieces[x_counter].m_get_status():
				#this piece is out of play - set up a dummy which will never get hit
				x_forecast_pointers[x_counter][0] = x_counter
				x_forecast_pointers[x_counter][1] = 999
				x_forecast_pointers[x_counter][2] = 0
			else:
				#otherwise, put in a forecast of where it would land based on the dice roll
				x_forecast_pointers[x_counter][0] = x_counter
				x_forecast_pointers[x_counter][1] = x_player.p_pieces[x_counter].m_get_location() * self.g_dievalue
				x_forecast_pointers[x_counter][2] = 0

		#now for each potential location see if there is a match in the opponent's pieces

		for x_counter_o in range (1,5):
			if not x_temp_opp.p_pieces[x_counter_o].m_get_status():
				#opp position is out of play and should be ignored -  dummy value
				x_logstring = "Ignoring target piece " + str(x_counter_o) + " as it is out of play."
				self.g_logmove(x_logstring)
				x_temp_opp_location = 888
			else:
				#hold the location of a potential target piece to hit
				x_temp_opp_location = x_temp_opp.p_pieces[x_counter_o].m_get_location()

			for x_counter_p  in range (1,5):
				#check that the locations match and that the opponents piece  is not at the start, or inactive:
				if x_forecast_pointers[x_counter_p][1] == x_temp_opp_location and x_temp_opp_location != 1 and x_temp_opp_location != 888:
					#we have a potential target
					x_forecast_pointers[x_counter_p][2] = 1
					x_logstring = "Player " + str(x_temp_opp.p_get_playerid()) + "'s marker " + str(x_counter_o) + " at location " + str(x_temp_opp.p_pieces[x_counter_o].m_get_location())  + " is a target of piece " + str(x_counter_p)
					self.g_logmove(x_logstring)
					break
				else:
					pass

			#move on to next player piece

		 #move on to next opponent piece


		#clear the array of player's pieces that are not a likely hit
		x_test_count_flag = False

		for x_counter_test in range (1,5): 
			if x_forecast_pointers[x_counter_test][2] == 1:
				#found at least one
				x_test_count_flag = True
			else:
				x_forecast_pointers[x_counter_test][0] = 999

		#got at least one potential target
		if x_test_count_flag:
			x_counter = 0
			while not x_found_target:
				x_counter = random.randint(1,4)
				if x_forecast_pointers[x_counter][0] != 999:
					x_piece_pointer = x_forecast_pointers[x_counter][0]
					x_logstring = "Player " + str(x_player.p_get_playerid()) + " has targets to consider and chose to move piece " + str(x_piece_pointer)
					self.g_logmove(x_logstring)
					self.g_marker_move(x_player.p_get_playerid(), x_piece_pointer)
					x_found_target = True
					return x_found_target
		else:
			x_logstring = "Player " + str(x_player.p_get_playerid()) + " could not find a clash target so is going to find a pointer at random to move."
			self.g_logmove(x_logstring)

			#toss up between on or off board
			x_offboard_flag = False

			x_onboard_flag = False
			for x_counter in range (1,5):
				#loop and see if there is a mix of on-board or off-board marker; do a coin toss if there is
				if x_player.p_pieces[x_counter].m_get_location() == 1 and x_player.p_pieces[x_counter].m_get_status():
					x_offboard_flag = True  #we could get a piece off the board
				else:
					pass
				if x_player.p_pieces[x_counter].m_get_location() > 1 and x_player.p_pieces[x_counter].m_get_status():
					x_onboard_flag = True  # we could get a piece on the board
				else:
					pass
			
			if x_onboard_flag:
				if x_offboard_flag:
					#choice is a wonderful thing - 1 is on-board, 2 is off-board
					x_temp_branch = random.randint(1,2) 
				else:
					x_temp_branch = 1
			
			if x_temp_branch == 1:
				x_piece_pointer = 0
				self.g_logmove("Finding a piece on the board.")
				x_piece_pointer = self.g_find_to_move_in_play(x_player)


				if x_piece_pointer != 0:
					#found one... move it        
					self.g_marker_move(x_player.p_get_playerid(), x_piece_pointer)
					x_found_target = True
				else:
					#didn't find one, have to force to go down the SET D path.
					x_temp_branch = 0
					x_found_target = False

			if x_temp_branch == 0:
				x_found_target = False
				self.g_logmove("Finding a piece OFF the board using SET D.")
			else:
				pass
		
		return x_found_target

	def g_get_playerturn(self):
		#this is a test
		    return self.g_playerturn
