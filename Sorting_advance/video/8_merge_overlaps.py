# Merge Overlapping Intervals
# Given a collection of intervals, merge all overlapping intervals.
# For example: Given [1,3],[2,6],[8,10],[15,18], return [1,6],[8,10],[15,18].

# Naive solution: TC = O(n**3) can be reduced to O(n**2)

# For every interval x, do:
# 1. check if x overlaps with other intervals. in case of merge:
# a. update x
# b. delete the other interval


# Efficient solution: TC = O(nlogn) SC = O(1)
# 1. Sort the intervals based on start time
# 2. Linearly traverse the sorted intervals and merge them if they overlap

def mergeIntervals(arr):
    arr.sort(key = lambda x: x[0])
    res = 0

    for i in range(1, len(arr)):
        if (arr[res][1] >= arr[i][0]):
            arr[res][1] = max(arr[res][1], arr[i][1])
        else:
            res = res+1
            arr[res] = arr[i]
    
    for i in range(res+1):
        print(arr[i], end=" ")

arr = [[5,10], [3,15], [18,30], [2,7]]

mergeIntervals(arr) # [2,15] [18,30]