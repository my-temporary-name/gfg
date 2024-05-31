# Rotate matrix by 90 degree
# 1 2 3     3 6 9
# 4 5 6 --> 2 5 8
# 7 8 9     1 4 7

arr = [[1,2,3],[4,5,6],[7,8,9]]

# Naive Approach: Time Complexity: O(n^2), space Complexity: O(n^2)
# 1. Last column become first row
# 2. Second last column become second row
# and so on

n = len(arr)

temp = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        temp[n-j-1][i] = arr[i][j] # What we are doing is assigning first row to first column in reverse order

for i in range(n):
    for j in range(n):
        arr[i][j] = temp[i][j]

for i in arr:
    print(i)

print("="*20)

# Efficient Approach: Time Complexity: O(n^2), space Complexity: O(1)

# 1. find transpose matrix
# 2. Reverse the rows
arr = [[1,2,3],[4,5,6],[7,8,9]]
n = len(arr)

for i in range(n):
    for j in range(i+1,n):
        arr[i][j], arr[j][i] = arr[j][i] , arr[i][j]

for i in range(n):
    low =0
    high =n-1

    while low<high:
        arr[low][i], arr[high][i] = arr[high][i], arr[low][i]
        low+=1
        high-=1

for i in arr:
    print(i)
