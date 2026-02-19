# ai.py

import random
from game import check_winner

def easy_ai(board):
    empty = [i for i in range(9) if board[i] == ""]
    return random.choice(empty)


def medium_ai(board, player, ai):
    # Try to win
    for i in range(9):
        if board[i] == "":
            board[i] = ai
            if check_winner(board) == ai:
                board[i] = ""
                return i
            board[i] = ""

    # Try to block
    for i in range(9):
        if board[i] == "":
            board[i] = player
            if check_winner(board) == player:
                board[i] = ""
                return i
            board[i] = ""

    return easy_ai(board)


def minimax(board, is_max, player, ai):
    result = check_winner(board)

    if result == ai:
        return 1
    elif result == player:
        return -1
    elif result == "Draw":
        return 0

    if is_max:
        best = -100
        for i in range(9):
            if board[i] == "":
                board[i] = ai
                score = minimax(board, False, player, ai)
                board[i] = ""
                best = max(best, score)
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == "":
                board[i] = player
                score = minimax(board, True, player, ai)
                board[i] = ""
                best = min(best, score)
        return best


def hard_ai(board, player, ai):
    best_score = -100
    move = 0

    for i in range(9):
        if board[i] == "":
            board[i] = ai
            score = minimax(board, False, player, ai)
            board[i] = ""
            if score > best_score:
                best_score = score
                move = i

    return move
