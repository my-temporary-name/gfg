# Rat in a Maze Problem
# Given a maze, NxN matrix. 
# A rat has to find a path from source to destination. maze[0][0] (left top corner)is the source and maze[N-1][N-1](right bottom corner) is the destination. 
# There are few cells which are blocked, means rat cannot enter into those cells.
# Only two moves are allowed:
# 1. (i+1, j) i.e down
# 2. (i, j+1) i.e right


def printsolution(sol):
    N = len(maze)
    for i in range(N):
        for j in range(N):
            print(sol[i][j], end=" ")
        print()

def isSafe(maze, i, j):
    return i<len(maze) and j<len(maze) and maze[i][j]==1 # if the cell is within the maze and it is not blocked

def solveMaze(maze):
    n = len(maze)
    sol = [[0 for j in range(n)] for i in range(n)] # initialize the solution matrix with 0

    if solveMazeRec(maze,0,0,sol) == False:
        print("Solution doesn't exist")
        return False
    printsolution(sol)

    return True

def solveMazeRec(maze, i, j, sol):
    if i==len(maze)-1 and j==len(maze)-1 and maze[i][j]==1: # if the rat reaches the destination
        sol[i][j]=1
        return True
    
    if isSafe(maze,i,j)==True: # if the cell is safe to move
        sol[i][j]=1

        if solveMazeRec(maze, i+1, j, sol)==True: # move down
            return True
        if solveMazeRec(maze, i, j+1, sol)==True: # move right
            return True
        sol[i][j]=0
    return False

maze = [[1,0,0,0],
        [1,1,0,1],
        [0,1,0,0],
        [1,1,1,1]]
        
solveMaze(maze)