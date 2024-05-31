arr = [[1,2,3],[4,5,6],[7,8,9]]

for r in arr:
    for x in r:
        print(x,end=" ")
    print()

print("=========")
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j],end=" ")
    print()


# User specified dimension

rows = 3
cols = 4

# Not recommended way
arr=[[0]*cols]*rows 
arr[0][0]=1 # This will assign 1 to all the elements of first column

for r in arr:
    print(r)

# Recommended way
print("=-=======================")

arr= [[0 for i in range(cols)] for j in range(rows)]
arr[0][0] = 1
for r in arr:
    print(r)