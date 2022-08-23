from random import randint as rand
from time import sleep


def display_board():
	for row in board:
		for col in row:
			print('|',col,  end="")
		print('\n')


def empty_space_remaining(board):
	found_empty = any(" " in sublist for sublist in board)
	if found_empty:
		return True
	else:
		return False


def is_winner(board, player):
	for row in range(len(board)):
		for col in range(len(board)):
			if board[row][col]==" ":
				continue
			try:
				if (board[0][0] == player and board[0][1] == player and board [0][2]==player) or (board[1][0] == player and board[1][1] == player and board [1][2]==player) or (board[2][0] == player and board[2][1] == player and board [2][2]==player):
					return True
				elif (board[0][0] == player and board[1][0] == player and board [2][0]==player) or (board[0][1] == player and board[1][1] == player and board [2][1]==player) or (board[0][2] == player and board[1][2] == player and board [2][2]==player):
					return True
				elif (board[0][0] == player and board[1][1] == player and board [2][2]==player):
					return True
				elif (board[2][0] == player and board[1][1] == player and board [0][2]==player):
					return True
			except:
				continue


def minimax(board, depth, isMaximizing):	
	if is_winner(board, ai_player):
		return -1
	elif is_winner(board, human_player):	
		return 1
	elif not empty_space_remaining(board):	
		return 0
	
	if isMaximizing is True:
		
		best_score = -800   #intialize to a very small score
		for row in range(len(board)):
			for col in range(len(board)):
				if board[row][col]==" ":
					board[row][col] = human_player
					score = minimax(board,depth+1,not isMaximizing)
					board[row][col] = " "
					best_score = max(score, best_score)
		return best_score
	else:
		
		best_score = 800       #intialize to a very big score
		for row in range(len(board)):
			for col in range(len(board)):
				if board[row][col]==" ":
					board[row][col] = ai_player
					score = minimax(board,depth+1,not isMaximizing)
					board[row][col] = " "
					best_score = min(score, best_score)
		return best_score

#Driver Code

board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
space_occupied = 0
best_score = 800
human_player = 'X'
ai_player = 'O'
game_over = False
current_player = human_player


while not game_over:
	display_board()
	if not empty_space_remaining(board):
		print("Game Over")
		game_over = True
		break	

	if is_winner(board, ai_player):
		print('Ai Winner! ')
		break
	elif is_winner(board, human_player):
		print("Human wins")
		break

	if current_player is human_player:
		print("Your turn: ")
		row_inp = int(input("Enter row: "))
		col_inp = int(input("enter Col: "))
		if board[row_inp][col_inp]==' ':
			board[row_inp][col_inp] = human_player
			current_player = ai_player
		else:
			print("already occupied, choose another spot! ")
			continue

	else:
		print("AI turn: ")
		best_score = 200
		for row in range(len(board)):
			for col in range(len(board)):		
				if board[row][col]==" ":
					board[row][col] = ai_player   
					score = minimax(board,0,True)
					board[row][col] = " "    #undo

					if score < best_score:   #AI Player Trying to minimize
						best_score = score 
						best_move = (row, col)
						
		board[best_move[0]][best_move[1]] = ai_player
		current_player = human_player


