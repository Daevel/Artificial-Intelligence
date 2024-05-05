"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)

    if x_count <= o_count:
        return X  
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possibleActions.add((i,j))

    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    if board[i][j] != EMPTY:
        raise Exception("Invalid action")

    new_board = [row[:] for row in board]  # Deep copy the board
    new_board[i][j] = player(board)

    return new_board


    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    lines = board + list(zip(*board)) + \
            [[board[i][i] for i in range(3)], [board[i][2 - i] for i in range(3)]]

    for line in lines:
        if len(set(line)) == 1 and line[0] is not EMPTY:
            return line[0]

    return EMPTY


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not EMPTY or all(all(cell is not EMPTY for cell in row) for row in board)


def utility(board):
    """
    Returns the utility of the current board state.
    """
    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def _minimax(board, maximizing_player):
        if terminal(board):
            return utility(board), None
        
        if maximizing_player:
            max_score = float('-inf')
            best_move = None
            for action in actions(board):
                new_board = result(board, action)
                score, _ = _minimax(new_board, False)
                if score > max_score:
                    max_score = score
                    best_move = action
            return max_score, best_move
        else:
            min_score = float('inf')
            best_move = None
            for action in actions(board):
                new_board = result(board, action)
                score, _ = _minimax(new_board, True)
                if score < min_score:
                    min_score = score
                    best_move = action
            return min_score, best_move
        
    _, best_move = _minimax(board, player(board) == X)
    return best_move
