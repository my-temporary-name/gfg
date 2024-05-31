# Search in Row and Column wise Sorted Matrix

# 10 20 30
# 15 25 35
# 27 29 35

# Find x = 29
# found at (2,1)

# Naive Approach is to scan whole 2D array. TC= O(RxC)

# Efficient Approach:

# 1. Begin from top right corner.
# 2. if x is same print and return
# 3. if x is smaller move left
# 4. if x is greater move down

def searchMatrix(arr,x):
    r = len(arr)
    c= len(arr[0])

    i=0
    j=c-1

    while i<r and j>=0:
        if arr[i][j]==x:
            print(f"found at [{i},{j}]")
            return
        elif arr[i][j]>x:
            j-=1
        else:
            i+=1
    print("Not found")


# Example usage
mat = [[10, 20, 30, 40],
       [15, 25, 35, 45],
       [27, 29, 37, 48],
       [32, 33, 39, 50]]

target = 50
searchMatrix(mat, target)