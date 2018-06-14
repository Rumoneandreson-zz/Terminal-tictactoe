import random
import os


def choose_player_marker():
    while True:
        choice = input("Choose a marker (X or O): ").upper()
        if choice == 'X' or choice == 'O':
            break

    if choice == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def play_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def display_board(board):
    print(board[9] + " | " + board[8] + " | " + board[7])
    print(board[4] + " | " + board[5] + " | " + board[6])
    print(board[1] + " | " + board[2] + " | " + board[3])


def choose_slot():
    # implement better check on the value the use inputs
    while True:
        slot_choice = int(input("Place mark in slot (0 - 9): "))
        if not slot_choice < 0 or slot_choice > 9:
            break

    return slot_choice


def add_slot(board, marker, slot):
    board[slot] = marker


def winner_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def game(board, player, player_turn):
    choice = choose_slot()
    # check if slot available
    while board[choice] != ' ':
        print("Cannot use this slot")
        choice = choose_slot()
        display_board(board)
        os.system("clear")

    add_slot(board, player, choice)
    if winner_check(board, player):
        return 'You Won'
    else:
        if ' ' in board:
            if player_turn == 'Player 1':
                return 'Player 2'
            else:
                return 'Player 1'
        else:
            return 'Game Tie'


def main_game():
    while True:
        print("TIC-TAC-TOE")
        board = [' '] * 10
        board[0] = 'n'
        # SETUP GAME
        # DETERMINE PLAYER MARKER
        player1, player2 = choose_player_marker()
        # Determine which player goes first
        player_turn = play_first()
        print(player_turn + " will go first")

        while True:
            print(player_turn + " Turn ")
            if player_turn == 'Player 1':
                player_turn = game(board, player1, player_turn)
            else:
                player_turn = game(board, player2, player_turn)

            if player_turn == 'You Won' or player_turn == 'Game Tie':
                print(player_turn)
                break

            display_board(board)
            os.system("clear")

        continue_play = input("Do you want to play again (Y on N): ").upper()
        os.system("clear")
        if continue_play == 'N':
            break


main_game()

