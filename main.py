'''
write a program to create tictac game
first create board to display tictac game

'''


# from IPython.display import clear_output


def display_board(board):
    # to clear previous output
    print('\n' * 100)
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |   ")
    print("...........")
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |   ")
    print("...........")
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |   ")


# board=[' ']*10
# print(board)
# display_board(board)


'''
step 2
Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'.
Think about using while loops to continually ask until you get a correct answer.
'''


def player_input():
    marker = ' '
    # output = return (player1_marker,player2_marker)
    while marker != 'X' and marker != 'O':
        marker = input("Player 1: Do you want to be X or O").upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# player1_marker,player2_marker=player_input()
# print(player1_marker)
# print(player2_marker)

'''
Step 3: Write a function that takes in the board list object,
a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
'''


def place_marker(board, marker, position):
    board[position] = marker


# place_marker(board,'X',7)
# display_board(board)


'''
Step 4: Write a function that takes in a board and checks to see if someone has won.
'''


def win_check(board, marker):
    return ((board[1] == marker and board[2] == marker and board[3] == marker) or
            (board[4] == marker and board[5] == marker and board[6] == marker) or
            (board[7] == marker and board[8] == marker and board[9] == marker) or
            (board[7] == marker and board[4] == marker and board[1] == marker) or
            (board[8] == marker and board[5] == marker and board[2] == marker) or
            (board[9] == marker and board[6] == marker and board[3] == marker) or
            (board[7] == marker and board[5] == marker and board[3] == marker) or
            (board[1] == marker and board[5] == marker and board[9] == marker))


# print(win_check(board,'X'))

'''
Step 5: Write a function that uses the random module to randomly decide 
which player goes first. You may want to lookup random.randint() Return a string of which player went first.

'''
import random


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player1'
    else:
        return 'Player2'


'''
Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.
'''


def space_check(board, position):
    return board[position] == ' '


'''
Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
'''


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    # board is return True when board is full
    return True


'''
Step 8: Write a function that asks for a player's next position (as a number 1-9) and
then uses the function from step 6 to check if its a free position. If it is, then return the position for later use.
'''


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position


'''

Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.
'''


def replay():
    choice = input('Do you want to play again? Enter Yes or No: ')
    return choice == 'Yes'


'''
step 10
Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!
'''

print("Welcome to tic tac toe!!!")
# while() to continue run the game
while True:
    # play the game
    # reset the board
    # set everything up board,whose first,choose marker X or O
    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + "will go first")
    play_game = input("Ready To play enter y/n ?")
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == "Player1":
            display_board(board)
            # choose position
            position = player_choice(board)
            place_marker(board, player1_marker, position)
            # place marker on that position
            if win_check(board, player1_marker):
                display_board(board)
                print("Player 1 has won")
                game_on = False
                # check if they won or tie
            else:
                # if they tie
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player2'






        else:
            # player2 Turn
            display_board(board)
            # choose position
            position = player_choice(board)
            place_marker(board, player2_marker, position)
            if win_check(board, player2_marker):
                display_board(board)
                print("Player 2 has won")
                game_on = False
                # check if they won or tie
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player1'

    if not replay():
        break
        # choice is not true that means it is false
        # break out of while loop




































