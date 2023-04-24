# simple game which pretends to play tic-tac-toe with the user

from random import randrange
 

def create_grid():
# This function creates a playboard with first computer move on position 5
    print("Here is the playboard: ")
    board = [["1", "2", "3"],
             ["4", "X", "6"],
             ["7", "8", "9"]]        
    return board

#Function accepts one parameter containing the board's current status and prints it out to the console.
def display_board(board):
    rows = len(board)
    cols = len(board)
    print("+---+---+---+")
    for r in range(rows):
        print("|",board[r][0], "|",board[r][1], "|",board[r][2],"|")
        print("+---+---+---+")
    return board

#Function accepts the board's current status, asks the user about their move, 
# checks the input, and updates the board according to the user's decision.
def enter_move(board):
	ok = False	# fake assumption - we need it to enter the loop
	while not ok:
		move = input("Enter your move: ") 
		ok = len(move) == 1 and move >= '1' and move <= '9' # is input valid?
		if not ok:
			print("Bad move - repeat your input!") # no, it isn't - do the input again
			continue
		move = int(move) - 1 # cell's number from 0 to 8
		row = move // 3 	# cell's row
		col = move % 3		# cell's column
		sign = board[row][col]	# check the selected square
		ok = sign not in ['O','X'] 
		if not ok:	# it's occupied - to the input again
			print("Field already occupied - repeat your input!")
			continue
	board[row][col] = 'O' 	# set '0' at the selected square
        

def make_list_of_free_fields(board):
#function browses the board and builds a list of all the free squares; 
#the list consists of tuples, while each tuple is a pair of row and column numbers.
    free =[]
    for row in range(3): # iterate through rows
        for col in range(3): # iterate through columns
            if board[row][col] not in ['O','X']: # is the cell free?
                free.append((row,col)) #it is - append new tuple to the list
    return free


#Function analyzes the board's status in order to check if the player using 'O's or 'X's has won the game
def victory_for(board,sgn):
	if sgn == "X":	# are we looking for X?
		who = 'me'	# yes - it's computer's side
	elif sgn == "O": # ... or for O?
		who = 'you'	# yes - it's our side
	else:
		who = None	# we should not fall here!
	cross1 = cross2 = True  # for diagonals
	for rc in range(3):
		if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:	# check row rc
			return who
		if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn: # check column rc
			return who
		if board[rc][rc] != sgn: # check 1st diagonal
			cross1 = False
		if board[2 - rc][2 - rc] != sgn: # check 2nd diagonal
			cross2 = False
	if cross1 or cross2:
		return who
	return None


def draw_move(board):
# Function draws the computer's move and updates the board.
    free = make_list_of_free_fields(board) # make a list of free fields
    free_place = len(free)
    if free_place > 0:	# if the list is not empty, choose a place for 'X' and set it
        this = randrange(free_place)   
        row, col = free[this]
        board[row][col] = 'X'

def main():
# The main function
    board = create_grid()
    free =make_list_of_free_fields(board)
    human_turn = True 
    while len(free):
        display_board(board)
        if human_turn:
            enter_move(board)
            victor = victory_for(board,'O')
        else:	
            draw_move(board)
            victor = victory_for(board,'X')
        if victor != None:
            break
        human_turn = not human_turn		
        free = make_list_of_free_fields(board)

    display_board(board)
    if victor == 'you':
        print("You won!")
    elif victor == 'me':
        print("I won!\nOne more try?")
    else:
        print("Tie!")
    
main()