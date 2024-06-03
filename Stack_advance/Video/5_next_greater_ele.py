# Next Greater Element
# Given an array of integers, find the next greater element for every element in the array. If a next greater element is not found, print -1.
# Example: [15, 10, 18, 12, 4, 6, 2, 8]
# Output:   18, 18, -1, -1, 6, 8, 8, -1

# Naive Approach: O(n^2)
# Use two loops to find the next greater element for every element in the array.

def printNextGreater(arr):
    
    for i in range(len(arr)):
        ng = -1
        for j in range(i+1,len(arr)):
            if arr[j]>arr[i]:
                ng = arr[j]
                break
        print(ng,end=" ") 
    
arr = [15, 10, 18, 12, 4, 6, 2, 8]

printNextGreater(arr)

# Efficient Approach: O(n), Space: O(n)

def nextGreater(arr):
    st = []
    n=len(arr)
    res = [None]*n # Here we are storing the next greater element for each element in the array
    for i in range(n-1,-1,-1):
        while len(st)>0 and st[-1]<=arr[i]:
            st.pop()
        res[i] = -1 if len(st)==0 else st[-1]
        st.append(arr[i])
    
    for x in res:
        print(x,end=" ")

arr = [15, 10, 18, 12, 4, 6, 2, 8]
print()
nextGreater(arr)