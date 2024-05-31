# Transpose of Matrix
# 1 2 3    1 4 7
# 4 5 6 -->2 5 8
# 7 8 9    3 6 9
def transpose(arr):
    n=len(arr)
    m=len(arr[0])

    # for i in range(m):
    #     for j in range(n):
    #         print(arr[j][i],end=" ")
    #     print()

    temp =[[0*n for i in range(n)] for j in range(m)]

    for i in range(m):
        for j in range(n):
            temp[i][j] = arr[j][i]
    # for i in arr:
    #     print(i)
    # for i in temp:
    #     print(i)

arr = [[1,2,3,33],[4,5,6,33],[7,8,9,33]]

transpose(arr)


# Efficient approach

arr = [[1,2,3],[4,5,6],[7,8,9]]

n = len(arr)

# Only for square matrix
for i in range(n):
    for j in range(i+1,n):
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

for i in arr:
    print(i)