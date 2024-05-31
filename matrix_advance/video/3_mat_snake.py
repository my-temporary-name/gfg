# Print matrix in snake patter
# 1 2 3 
# 4 5 6
# 7 8 9

# Output should be: 1 2 3 6 5 4 7 8 9

def printSnake(arr):
    n = len(arr)
    m = len(arr[0])

    for i in range(n):
        if i%2==0:
            for j in range(m):
                print(arr[i][j], end=" ")
        else:
            for j in range(m-1,-1,-1):
                print(arr[i][j], end = " ")



arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
printSnake(arr)
