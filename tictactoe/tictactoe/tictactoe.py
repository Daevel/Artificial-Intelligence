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

    if x_count <= o_count:  # Controlla se il numero di 'X' è minore o uguale al numero di 'O'
        return 'X'  # Il giocatore 'X' ha sempre il primo turno
    else:
        return 'O'
    #raise NotImplementedError


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
  
    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)

    current_player = player(new_board)
    i,j = action
    action = (i, j)
    print(i)
    print(j)
    print(action)


    if new_board[i][j] != EMPTY:
        raise Exception("Invalid action")
    
    new_board[i][j] = current_player


    return new_board


    #raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    

    # Check rows for winner
    for row in board:
        if len(set(row)) == 1 and row[0] != EMPTY:
            return row[0]

 
    # Check columns for winner
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            
            return board[0][col]

    # Check diagonals for winner
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
       
        return board[0][2]
    

    # No winner
    return EMPTY
    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not EMPTY:

        return True
    
    for row in board:
        for cell in row:
            if cell == EMPTY:
            
                return False

    
    else:
        return True
    #raise NotImplementedError


def utility(board):
        # Controllo righe
        for row in board:
            if all(cell == 'X' for cell in row):
                return 1
            elif all(cell == 'O' for cell in row):
                return -1
        # Controllo colonne
        for col in range(3):
            if all(board[row][col] == 'X' for row in range(3)):
                return 1
            elif all(board[row][col] == 'O' for row in range(3)):
                return -1
        # Controllo diagonali
        if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2-i] == 'X' for i in range(3)):
            return 1
        elif all(board[i][i] == 'O' for i in range(3)) or all(board[i][2-i] == 'O' for i in range(3)):
            return -1
        # Nessuno ha vinto
        return 0
    #raise NotImplementedError


def minimax(board):
    def _minimax(board, maximizing_player):
        score = utility(board)
        if score != 0:
            return score, None
        
        empty_spaces = [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]
        
        if not empty_spaces:
            return 0, None
        
        if maximizing_player:
            max_score = float('-inf')
            best_move = EMPTY
            for move in empty_spaces:
                board[move[0]][move[1]] = 'X'
                score, _ = _minimax(board, False)
                if score > max_score:
                    max_score = score
                    best_move = move
                board[move[0]][move[1]] = EMPTY
                
            return max_score, best_move
        else:
            min_score = float('inf')
            best_move = EMPTY
            for move in empty_spaces:
                board[move[0]][move[1]] = 'O'
                score, _ = _minimax(board, True)
                if score < min_score:
                    min_score = score
                    best_move = move
                board[move[0]][move[1]] = EMPTY
             
            return min_score, best_move
        
    _, best_move = _minimax(board, True)
    return best_move
