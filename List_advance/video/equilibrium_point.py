# Equilibrium Point
# Point is an equilibrium point if sum of elements before it is equal to sum of elements after it.
# example: [3,4,8,-9,20,6]; Output: True i.e 20 is an equilibrium point as 3+4+8-9 = 6
# [4,2,-2]; Output: True i.e 4 is an equilibrium point as 0 = 2-2

# Naive solution: Time Complexity: O(n^2)

def ePoint(arr):
    n= len(arr)
    for i in range(n):
        ls,rs=0,0
        for j in range(i):
            ls+=arr[j]
        for k in range(i+1,n):
            rs+=arr[k]
        
        if (ls==rs):
            return True
    return False

arr = [3,4,8,-9,20,6]
print("Is there an equilibrium point: ",ePoint(arr)) # Output: True

# Efficient solution: Time Complexity: O(n) and Space Complexity: O(n)
# 1. Compute Prefix sum array
# 2. Compute Suffix sum array
# 3. For every element (except corner ones), check if ps[i-1] is same as ss[i+1]

# More efficient solution: Time Complexity: O(n) and Space Complexity: O(1)

def ePoint(arr):
    rs = sum(arr)
    ls = 0
    for i in range(len(arr)):
        rs-=arr[i]
        if ls==rs:
            return True
        ls+=arr[i]
    return False

arr=[3,4,8,-9,20,6]
print("Is there an equilibrium point: ",ePoint(arr)) # Output: True

# Another question: Given array check if it can be partitioned into 3 different parts with equal sum.
# Example: [5,2,6,1,1,1,1,4]; Output: True i.e 5+2 = 6+1 = 1+1+1+4 => 7
