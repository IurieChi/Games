# simple game which pretends to play tic-tac-toe with the user

from random import randrange
 
# for i in range(10):
#     print(randrange(8))
# board[row][column]

def create_grid():
# This function creates a blank playboard
    print("Here is the playboard: ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]        
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


# def enter_move(board):
#     # The function accepts the board's current status, asks the user about their move, 
#     # checks the input, and updates the board according to the user's decision.


# def make_list_of_free_fields(board):
#     # The function browses the board and builds a list of all the free squares; 
#     # the list consists of tuples, while each tuple is a pair of row and column numbers.


# def victory_for(board, sign):
#     # The function analyzes the board's status in order to check if 
#     # the player using 'O's or 'X's has won the game


# def draw_move(board):
#     # The function draws the computer's move and updates the board.

table= create_grid()
display_board(table)