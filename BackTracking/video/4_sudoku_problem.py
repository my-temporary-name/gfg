# Sudoku Problem
# Given a 9x9 matrix, where each row, column and each 3x3 subbox contains the number from 1 to 9.
# Check if the given matrix is valid sudoku or not.
# Return 0 if the given matrix is not valid, else return 1.
# A sudoku is considered valid if according to the rules:
# 1. Each row contains the numbers from 1 to 9 exactly once.
# 2. Each column contains the numbers from 1 to 9 exactly once.
# 3. Each 3x3 subgrid contains the numbers from 1 to 9 exactly once.
# Note:
# 1. A 1 is used to fill the empty cells.
# 2. There may be more than one solution to a given sudoku.
# 3. The given A does not contain invalid sudoku.


# In our problem, we will be given a matrix with vacant cells denoted by 0.
# Return the completed sudoku matrix if it is valid, else return -1.

# Each row and each column should contain the numbers from 1 to N exactly once. for NxN matrix

import math

def isSafe(board,row,col,num): # check if the number is safe to place at the given position
    
    N = len(board)
    
    for d in range(N): # check if the number is present in the row or column
        
        if board[row][d]== num:
            return False
            
    for r in range(N): # check if the number is present in the 3x3 subgrid
        if board[r][col]==num:
            return False 
    s = int(math.sqrt(N))
    boxRowStart = row  - row%s  # find the starting row of the 3x3 subgrid
    boxColStart = col - col%s  # find the starting column of the 3x3 subgrid
    
    for r in range(boxRowStart,boxRowStart+s): 
        for d in range(boxColStart,boxColStart+s):
            
            if board[r][d]==num:
                return False
    return True
        
def solve(board): # solve the sudoku
    N = len(board)
    row = -1
    col = -1
    isEmpty = True 
    
    for i in range(N):
        
        for j in range(N):
            
            if board[i][j]==0:
                row = i
                col = j 
                isEmpty = False
                break 
        if not isEmpty:
            break
    if isEmpty:
        return True
    for num in range(1,N+1): # check if the number is safe to place at the given position
        if isSafe(board,row,col,num):
            board[row][col]= num
            if solve(board):
                return True
            else:
                board[row][col]= 0
            
    return False
    
board = [[1,0,3,0],
        [0,0,2,1],
        [0,1,0,2],
        [2,4,0,0]]
        
solve(board)
print(board)
    