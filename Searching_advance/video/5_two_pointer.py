# Two Pointer Approach
# Find if there's a pair with a given sum in the array
# Example: [2,5,8,12,30], sum=17; Output: True

# Naive Approach: Time Complexity: O(n^2), Where we consider all possible pairs using two loops

# Efficient Approach: Time Complexity: O(n), Space Complexity: O(1) ; Using Two Pointer Approach
# We move i from start and j from end. If sum of arr[i] and arr[j] is less than sum, we move i to right, else we move j to left

def valid_pair(arr,x):
    i=0
    j=len(arr)-1

    while i<j:
        if arr[i]+arr[j]==x:
            return True
        elif arr[i]+arr[j] < x: # When sum is less than x, we need to increase the sum, so we move i to right
            i+=1
        else: # When sum is greater than x, we need to decrease the sum, so we move j to left
            j-=1
    return False

arr = [2,5,8,12,30]
x = 17
print("Pair with given sum is: ",valid_pair(arr,x))