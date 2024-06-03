# Largest Rectangle of 1s in a Binary Matrix; Return the area of the largest rectangle containing only 1s in a binary matrix.
# Example: [[1, 0, 1, 0, 0],
#           [1, 0, 1, 1, 1],
#           [1, 1, 1, 1, 1],
#           [1, 0, 0, 1, 0]]
# Output: 6

# Naive Approach: O(R**3 x C**3)
# 1. Consider every cell as starting point of the rectangle # O(RxC)
# 2. consider all sizes of rectangle with current cell as a starting point # O(RxC)
# 3. For the current rectangle , check if it has all 1s. if yes, then update the res if current area is greater than res # O(RxC)


# Efficient Approach: O(RxC)

# [0, 1, 1, 0] --> res = 2 [0, 1, 1, 0]
# [1, 1, 1, 1] --> res = 4 [1, 2, 2, 1]
# [1, 1, 1, 1] --> res = 8 [2, 3, 3, 2]
# [1, 1, 0, 0] --> res =88 [3, 4, 0, 0]

# Run a loop from 0 to R-1
# 1. Update the histogram for the current row
# 2. Find the largest area of the histogram and update the res if required


def largestHist(arr):
    st = []
    res = 0
    for i in range(len(arr)):
        while st and arr[st[-1]]>=arr[i]:
            tp = st[-1]
            st.pop()
            curr_width = (i-st[-1]-1) if st else i
            res = max(res, curr_width * arr[tp])
        st.append(i)
    
    while st:
        tp = st[-1]
        st.pop()
        curr_width = (len(arr) - st[-1]-1) if st else len(arr)
        res = max(res, curr_width*arr[tp])
    return res

def maxRectangle(mat):
    res = largestHist(mat[0])
    for i in range(1,len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j]:
                mat[i][j]+=mat[i-1][j]
            res = max(res, largestHist(mat[i]))
    return res

mat = [[1, 0, 1, 0, 0],
         [1, 0, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 0, 0, 1, 0]]

print(maxRectangle(mat)) # 6