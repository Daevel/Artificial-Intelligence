from tictactoe import winner, terminal, result, minimax

X = 'X'
O = 'O'
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[X, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

matrix = initial_state()

#result(matrix, (1,2))
minimax(matrix)
#terminal(matrix)
print(minimax)


#winner(matrix)

#print(winner)