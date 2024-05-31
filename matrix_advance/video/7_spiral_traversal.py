# Spiral Traversal of Matrix
# 1 2 3
# 4 5 6
# 7 8 9

# Output: 1 2 3 6 9 8 7 4 5

arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
for i in arr:
    print(i)

# Top row
# Right  column
# Bottom row (reversed)
# left column (reversed)

r =len(arr)
c = len(arr[0])

top =0
left =0
right = c-1
bottom = r-1

print("==========================")

while top<=bottom and left<=right:
    # Top row
    for i in range(left,right+1):
        print(arr[top][i],end= " ")
    top+=1

    # right column
    for i in range(top,bottom+1):
        print(arr[i][right], end=" ")
    right-=1

    # Bottom row
    if top<=bottom:
        for i in range(right,left-1, -1):
            print(arr[bottom][i], end=" ")
        bottom-=1
    
    # left column
    if left<=right:
        for i in range(bottom, top-1,-1):
            print(arr[i][left], end=" ")
        left+=1
    