# subset Sum problem: Given an array of integers and a target sum, find all unique combinations in the array whose sum is equal to the target sum.

def subset_sum(arr, n ,target): # Time complexity: O(2^n) ; Space complexity: O(n)
    if n==0:
        return 1 if target==0 else 0
    return subset_sum( arr, n-1, target ) + subset_sum( arr, n-1, target-arr[n-1] )