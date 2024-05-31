# Triple in Sorted Array
# Given the array and the sum, find if there exists a triplet in the array which gives the sum.

# Example = [2, 3, 4, 8, 9, 20, 40], sum=32; Output: True (4,8,20)

# Naive Approach: Time Complexity: O(n^3); Where we will run 3 loops to find the triplet (n), (i+1, n), (j+1, n)

# Efficient Approach: Time Complexity: O(n^2); Using Two Pointer Approach
# 1. Traverse the array from start to end
# 2. For each element, find the pair with the given sum using two pointer approach

def isPair(arr,x, si):
    i=si
    j = len(arr)-1
    while i<j:
        if arr[i]+arr[j]==x:
            return True
        elif arr[i]+arr[j] < x: # When sum is less than x, we need to increase the sum, so we move i to right
            i+=1
        else: # When sum is greater than x, we need to decrease the sum, so we move j to left
            j-=1
    return False

def triplet_sum(arr,x):
    for i in range(len(arr)-2):
        if (isPair(arr, x-arr[i], i+1)):
            return True
    return False

arr = [2, 3, 4, 8, 9, 20, 40]
x = 32
print("Triplet with given sum is: ",triplet_sum(arr,x))