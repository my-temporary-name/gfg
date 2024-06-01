# Chocolate Distribution Problem
# Given an array of n integers where each value represents number of chocolates in a packet. Each packet can have variable number of chocolates. 
# There are m students, the task is to distribute chocolate packets such that: the difference between maximum chocolates and minimum chocolates given to the students is minimum.

# Example: arr = [7, 3, 2, 4, 9, 12, 56], m = 3 : Output: 2  (2,3,4)

# Idea for solution:
# 1. Consider every items as minimum one by one ( and pick adjacent greater value) [7,9,12] , [3,4,7], [2,3,4], ....
# 2. minimum of all the values is 2

# Time complexity: O(nlogn)


def mindiff(arr,m):
    if m==0 or len(arr)==0:
        return 0
    if len(arr)<m:
        return -1
    arr.sort()
    res = arr[m-1] - arr[0]

    for i in range(1,len(arr)-m+1):
        res = min(res, arr[i+m-1]-arr[i])
    return res

arr = [7, 3, 2, 4, 9, 12, 56]
m = 3
print(mindiff(arr,m)) # 2