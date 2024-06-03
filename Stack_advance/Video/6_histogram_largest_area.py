# Largest Area in a Histogram
# https://www.youtube.com/watch?v=ZmnqCZp9bBs
# Given an array of integers, find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of contiguous bars. 
# For simplicity, assume that all bars have the same width and the width is 1 unit.

# Example: [6, 2, 5, 4, 1, 5, 6]
# Output: 10 # 5*2 in last 2 bars

# Naive Approach: O(n^2)

def getMaxArea(arr):
    res = 0
    for i in range(len(arr)):
        curr = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j]>=arr[i]:
                curr+=arr[i]
            else:
                break
        
        for j in range(i+1,len(arr)):
            if arr[j]>=arr[i]:
                curr+=arr[i]
            else:
                break
        
        res = max(res, curr)
    return res

arr = [6, 2, 5, 4, 1, 5, 6]
print(getMaxArea(arr))

# Efficient Approach: O(n), Space: O(n)
# Idea:
# 1. Initialize res = 0
# 2. Find previous smaller element for each element in the array
# 3. Find next smaller element for each element in the array
# 4. Do the following for each element in the array:
#  curr = arr[i]
#  curr+=(i - ps[i]-1) * arr[i] # ps[i] is the index of previous smaller element
#  curr+= (ns[i]-i-1) * arr[i] # ns[i] is the index of next smaller element
#  res = max(res, curr)
# 5. Return res


# More efficient approach: O(n), Space: O(n)
# Using single stack

def getMaxArea2(arr):
    st = []
    res = 0

    for i in range(len(arr)):
        while st and arr[st[-1]]>=arr[i]:
            tp = st[-1]
            st.pop()
            curr_width = (i - st[-1]-1) if st else i
            res = max(res, curr_width*arr[tp])
        st.append(i)

    while st:
        tp = st[-1]
        st.pop()
        curr_width = (len(arr)-st[-1]-1) if st else len(arr)
        res=max(res, curr_width*arr[tp])
    return res

arr = [6, 2, 5, 4, 1, 5, 6]
print(getMaxArea2(arr))