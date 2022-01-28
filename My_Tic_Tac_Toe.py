#!Python3
#Tic Tac Toe Game

import random


# Displays the Tic Tac Toe Board
def display_board(board):
    print("\n" * 30)
    print("            |        |           ")
    print("     " + board[1] + "      |    " + board[2] + "   |  " + board[3])
    print("            |        |           ")
    print("------------------------------------")
    print("            |        |           ")
    print("     " + board[4] + "      |    " + board[5] + "   |  " + board[6])
    print("            |        |           ")
    print("------------------------------------")
    print("            |        |           ")
    print("     " + board[7] + "      |    " + board[8] + "   |  " + board[9])
    print("            |        |           ")


# Ask user to chose X or O. (player1,player2 = player_input()) (player1,player2 = "X", "O") same as (player1 = "X"
# player2 = "O") or vise versa.
def player_input():
    marker = "wrong"
    while marker not in ["X", "O"]:
        marker = input("Player_1, Do you want to be X or O?\n").upper()

    if marker == "X":
        return "X", "O"
    else:
        return "O", "X"


# place either X or O on selected empty board position (board[5] = "X")
def place_marker(board, marker, position):
    board[position] = marker


# Returns True if matches 3 X's or 3 O's in a row
def win_check(board, mark):
    if board[3] == mark and board[5] == mark and board[7] == mark:  # diagonal
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:  # diagonal
        return True
    elif board[1] == mark and board[2] == mark and board[3] == mark:  # across the top
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:  # across the middle
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:  # across the bottom
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:  # down/up the left side
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:  # down/up the middle
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:  # down/up the right side
        return True



# chooses the player that goes first
def choose_first():
    first = random.randint(1, 2)
    if first == 1:
        return "Player_1"
    else:
        return "Player_2"


# check to see if position is available
def space_check(board, position):
    if board[position] == " ":
        return True
    else:
        return False


# returns True if board is full
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False  # its not full yet
    return True  # Its full and no more empty spaces


def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board, position):
        position = int(input(f'{turn} Choose your next position: (1-9)\n'))

    return position


def replay():
    return input('Do you want to play again? Enter Yes or No:\n').lower().startswith('y')


#############################################################################################
######################                   ####################################################
###################### Game logic starts ####################################################
######################                   ####################################################
#############################################################################################

print("Welcome to Tic-Tac-Toe Covid-19 edition!\n")

while True:  # first while loop will ask player1 X or O and ask if they are ready to play. if so enter second loop
    # else replay() function
    board_1 = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player1_marker, player2_marker = player_input()  # ask player1 to chose X or O and assign.
    turn = choose_first()  # turn will be random between player1 or player2
    print(f"{turn} will go first.")

    play_game = input(f"{turn} Are you ready to play? Enter Yes or No.\n")  # pause the first loop

    if play_game.lower()[0] == "y":  # if True jumps into next while loop
        game_on = True
    else:
        game_on = False  # else jumps to replay() function.

    while game_on:  # Second while loop will display board, ask for position, insert X or O in position, check for
        # win or full board (tie)

        if turn == "Player_1":  # player1 logic
            display_board(board_1)
            position = player_choice(board_1)  # stops the loop since its an input()
            place_marker(board_1, player1_marker, position)

            if win_check(board_1, player1_marker):
                display_board(board_1)
                print(f"Congratulations!, {turn} has won the game!")
                game_on = False
            else:
                if full_board_check(board_1):
                    display_board(board_1)
                    print("The game is a draw!")
                    break
                else:
                    turn = "Player_2"

        else:
            display_board(board_1)  # Player2 logic
            position = player_choice(board_1)
            place_marker(board_1, player2_marker, position)

            if win_check(board_1, player2_marker):
                display_board(board_1)
                print(f"Congratulations!, {turn} has won the game!")
                game_on = False
            else:
                if full_board_check(board_1):
                    display_board(board_1)
                    print("The game is a draw!")
                    break
                else:
                    turn = "Player_1"

    if not replay():
        break
