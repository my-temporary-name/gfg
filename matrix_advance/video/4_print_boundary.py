# Print Boundary elements
# 1 2 3
# 4 5 6
# 7 8 9

# Output: 1 2 3 6 9 8 7 4

def printBound(arr):
    R = len(arr)
    C= len(arr[0])

    if R==1:
        for i in range(C):
            print(arr[0][i], end=" ")

    elif C == 1:
        for i in range(R):
            print(arr[i][0],end = " ")
    
    else:
        for i in range(C):
            print(arr[0][i], end = " ")
        for i in range(1,R):
            print(arr[i][C-1], end=" ")
        for i in range(C-2,-1,-1):
            print(arr[R-1][i],end = " ")
        for i in range(R-2,0,-1):
            print(arr[i][0], end=" ")

# arr = [[1,2,3],[4,5,6],[7,8,9]]
arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
printBound(arr)