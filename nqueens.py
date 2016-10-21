# nrooks.py : Solve the N-Rooks problem!
# Professor David Crandall, August 2016
# a few changes by Prateek Srivastava, September 2016
# The N-rooks problem is: Given an empty NxN chessboard, place N rooks on the board so that no rooks
# can take any other, i.e. such that no two rooks share the same row or column.
# The N-queens problem is: Given an empty NxN chessboard, place N queens on the board so that no queens
# can take any other, i.e. such that no two queens share the same row or column or diagonal.

# This is N, the size of the board.
import time
from sys import argv
start_time = time.time()
N = int(argv[1])


# Count # of pieces in given row
def count_on_row(board, row):
    return sum(board[row])


# Count # of pieces in given column
def count_on_col(board, col):
    return sum([row[col] for row in board])

# Count # of pieces for a given square in the all the diagonals
def count_on_diag(board, row, col):
    left_upper_diagonal=0
    left_bottom_diagonal=0
    right_upper_diagonal=0
    right_bottom_diagonal=0
    i=1
    for r in range(0,N):
        for c in range(0,N):
            while (i>=0 and i<=max(row,col)):
                if(row-i>=0 and col-i>=0):
                    left_upper_diagonal+=board[row-i][col-i]
                if(row+i<N and col+i<N):
                    right_bottom_diagonal+=board[row+i][col+i]
                if (row - i >= 0 and col + i <N ):
                    right_upper_diagonal += board[row-i][col+i]
                if (row + i <N and col - i >= 0):
                    left_bottom_diagonal += board[row+i][col-i]
                i += 1
    return left_upper_diagonal+right_bottom_diagonal+right_upper_diagonal+left_bottom_diagonal

# Count total # of pieces on board
def count_pieces(board):
    return sum([sum(row) for row in board])


# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    return "\n".join([" ".join(["Q" if col else "_" for col in row]) for row in board])


# Add a piece to the board at the given position, and return a new board (doesn't change original)
def add_piece(board, row, col):
    return board[0:row] + [board[row][0:col] + [1, ] + board[row][col + 1:]] + board[row + 1:]


# Get list of successors of given board state

"""#successor1 function - solves nrooks only
def successors1(board):
    return [ add_piece(board, r, c) for r in range(0, N) for c in range(0,N) ]"""

#successor2 function - solves nrooks only
"""def successors2(board):
    piece_count = count_pieces(board)
    successor_boards=[]
    for c in range(0,N):
        for r in range(0,N):
            if piece_count < N :
                temp=add_piece(board, r, c)
                if count_pieces(temp)==piece_count+1:
                    successor_boards.append(temp)
    return successor_boards"""

# successors3 function - solves nrooks only
"""def successors3(board):
    piece_count = count_pieces(board)
    successor_boards = []
    for c in range(0, N):
        for r in range(0, N):
            if piece_count < N and count_on_row(board, r) < 1 and count_on_col(board, c) < 1:
                temp = add_piece(board, r, c)
                if count_pieces(temp) == piece_count + 1:
                    successor_boards.append(temp)
    return successor_boards"""

#nqueens_successors function
def nqueens_successors(board):
    piece_count = count_pieces(board)
    successor_boards = []
    for c in range(0, N):
        for r in range(0, N):
            if (piece_count < N and count_on_row(board, r) < 1 and count_on_col(board, c) < 1 and count_on_diag(board,r,c)<1):
                temp = add_piece(board, r, c)
                if count_pieces(temp) == piece_count + 1:
                    successor_boards.append(temp)
    return successor_boards

# check if board is a goal state
#goal_state_rooks
"""def is_goal(board):
    return count_pieces(board) == N and \
           all([count_on_row(board, r) <= 1 for r in range(0, N)]) and \
           all([count_on_col(board, c) <= 1 for c in range(0, N)])"""

#goal_state_queens
def is_goal(board):
    if count_pieces(board) == N:
        for r in range(0,N):
            if count_on_row(board, r) <= 1:
                for c in range(0, N):
                    if count_on_col(board, c) <= 1 and count_on_diag(board,r,c)<=1:
                        return True
                    else:
                        return False

# Solve n-rooks!
def solve(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
        for s in nqueens_successors(fringe.pop()):  #pop(0) can be used to implement BFS (1st method)
            if is_goal(s):
                return (s)
            fringe.append(s)
            # fringe.insert(0,s) can also be used to implement BFS(2nd method)
    return False

# The board is stored as a list-of-lists. Each inner list is a row of the board.
# A zero in a given square indicates no piece, and a 1 indicates a piece.

initial_board = [[0] * N] * N
print "Starting from initial board:\n" + printable_board(initial_board) + "\n\nLooking for solution...\n"
solution = solve(initial_board)

print printable_board(solution) if solution else "Sorry, no solution found. :("

print "%f minutes" % ((time.time() - start_time) / 60)                # http://stackoverflow.com/questions/1557571/how-to-get-time-of-a-python-program-execution