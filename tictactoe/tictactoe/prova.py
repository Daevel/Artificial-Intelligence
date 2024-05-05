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
#minimax(matrix)
#terminal(matrix)
#print(minimax)


#winner(matrix)

#print(winner)

###

# Definizione di alcuni stati della tabella di gioco
board1 = [
    [X, O, X],
    [O, X, O],
    [X, EMPTY, EMPTY]
]

board2 = [
    [X, EMPTY, EMPTY],
    [O, X, EMPTY],
    [O, EMPTY, EMPTY]
]

board3 = [
    [X, EMPTY, EMPTY],
    [EMPTY, O, EMPTY],
    [EMPTY, EMPTY, EMPTY]
]

res = minimax(board2)
print(res)
