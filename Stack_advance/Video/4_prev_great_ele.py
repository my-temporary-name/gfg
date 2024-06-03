# Previous Greater Element
# Given an array of integers, find the previous greater element for every element in the array. If a previous greater element is not found, print -1.

# eg:     [15, 10, 18, 12, 4, 6, 2, 8]
# output: -1, 15, -1, 18, 12, 12, 6, 12

# Naive Approach: O(n^2)
# Use two loops to find the previous greater element for every element in the array.

def prevGreater(arr):
    for i in range (len(arr)):
        pg = -1
        for j in range(i-1,-1,-1):
            if arr[j]> arr[i]:
                pg = arr[j]
                break
        print(pg,end=" ")
                
        
        
        
    
arr = [15, 10, 18, 12, 4, 6, 2, 8]

prevGreater(arr)

# Efficient Approach: O(n), Space: O(n)
# Similar to the stock span problem, we can use a stack to find the previous greater element for every element in the array.

def prevGreater2(arr):
    st = []
    for i in range(len(arr)):
        while len(st)>0 and st[-1]<=arr[i]:
            st.pop()
        pg = -1 if len(st)==0 else st[-1]
        print(pg,end=" ")
        st.append(arr[i])   

arr = [15, 10, 18, 12, 4, 6, 2, 8]
print()
prevGreater2(arr)