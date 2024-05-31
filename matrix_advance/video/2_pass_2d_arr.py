
def printmat(mat):
    n = len(mat)
    m = len(mat[0])

    for i in range(n):
        for j in range(m):
            print(mat[i][j], end=" ")
        print()


if __name__ == "__main__":
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    printmat(mat)