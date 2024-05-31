# prefix sum technique
# Given an array and a range, we need to find the sum of elements in that range.
# Example: [2,8,3,9,6,5,4], range=(1,3); Output: 20

# Naive solution: Time Complexity: O(n) or O(r-l+1)
# Here we just run for loop from start to end and add the elements in the range.

# We will use Pre-computation technique to solve this problem. # Time Complexity of query will be O(1)

arr =[2,8,3,9,6,5,4]
n=len(arr)
pSum = [None]*n
pSum[0] = arr[0]
for i in range(1,n):
    pSum[i] = pSum[i-1]+arr[i]


def getSum(l,r):
    if l==0:
        return pSum[r]
    else:
        return pSum[r] - pSum[l-1]

l,r = 1,3
print("Sum of elements in the range is: ",getSum(l,r)) # Output: 20

# What if there is weighted sum and we need to find the sum of elements in the range.

# Example: arr=[2,8,3,9,6,5,4], range=(1,3); Output: 1*2+2*8+3*3 = 27
                              # range=(2,3); Output: 1*3+2*9 = 21

# getWSum(l,r) = 1*arr[l]+2*arr[l+1]+3*arr[l+2]+...+(r-l+1)*arr[r]