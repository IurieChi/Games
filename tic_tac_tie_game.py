# simple game which pretends to play tic-tac-toe with the user

from random import randrange
 
# for i in range(10):
#     print(randrange(8))
# board[row][column]

def create_grid():
# This function creates a blank playboard
    print("Here is the playboard: ")
    board = [["1", "2", "3"],
             ["4", "X", "6"],
             ["7", "8", "9"]]        
    return board

def display_board(board):
#     # The function accepts one parameter containing the board's current status
#     # and prints it out to the console.
    rows = len(board)
    cols = len(board)
    print("+---+---+---+")
    for r in range(rows):
        print("|",board[r][0], "|",board[r][1], "|",board[r][2],"|")
        print("+---+---+---+")
    return board


def enter_move(board):
#     # The function accepts the board's current status, asks the user about their move, 
#     # checks the input, and updates the board according to the user's decision.
    choise = True
    while choise:
        move = input("Please select number for move ")
        choise = len(move) == 1 and move >= '1' and move <= '9' # is user's input valid
        if not choise:
            print("Bad move - repeat your input!")
            continue
        move = int(move) - 1 	# cell's number from 0 to 8
        row = move // 3 	# cell's row
        col = move % 3
        sign = board[row][col]	# check the selected square
        choise = sign not in ['O','X'] 
        if not choise:	# it's occupied - to the input again
            print("Field already occupied - repeat your input!")
            continue
        board[row][col] = 'O' 	# set '0' at the selected square
        display_board(table)

def make_list_of_free_fields(board):
#     # The function browses the board and builds a list of all the free squares; 
#     # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free =[]
    for row in range(3): # iterate through rows
        for col in range(3): # iterate through columns
            if board[row] [col] not in ['O','X']: # is the cell free?
                free.append((row,col)) # yes, it is - append new tuple to the list
    return free


# def victory_for(board, sign):
#     # The function analyzes the board's status in order to check if 
#     # the player using 'O's or 'X's has won the game


def draw_move(board):
#     # The function draws the computer's move and updates the board.
    free = make_list_of_free_fields(board) # make a list of free fields
    cnt = len(free)
    if cnt > 0:	# if the list is not empty, choose a place for 'X' and set it
        this = randrange(cnt)   
        row, col = free[this]
        board[row][col] = 'X'
        display_board(board)

table= create_grid()
display_board(table)
enter_move(table)
draw_move(table)
