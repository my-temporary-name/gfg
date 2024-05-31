# Median of Row wise sorted Matrix
# Every row is sorted in increasing order
# Odd size matrix
# All distinct elements


# Naive solution:
# 1. Put all elements in an array
# 2. Sort the array
# 3. Return the middle element
# TC = O(r x c x log(rxc))

# Efficient solution : TC: O( R x log(max-min)*log(c)) # Max: maximum element in matrix
# 5 10 20 30 40
# 1  2  3  4  6
# 11 13 15 17 19

# 1. Find min element, mn
# 2. Find max element, mx
# 3. Find target position, tpos = (r + c+ 1)/2
# 4. Do binary search starting from (mn +mx)/2

# tpos = (3*5+1)/2 = 8

# mn =1, mx = 40: mid = 20, ,midpos (where it lies in r*c numbers if sorted) = 3+5+5 =13 (at 13th index) ==>update max. Since tpos<midpos
# mn=1, mx =20: mid=10, midPos = 2+5+0=7 ==> update min
#....
# mn=11, mxx=11. Continue till both min and max are same
from bisect import bisect
def printMedian(arr):
    r,c = len(arr), len(arr[0])
    mn, mx = arr[0][0], arr[0][c-1]
    for i in range(1,r):
        mn = min(mn,arr[i][0])
        mx = max(mx, arr[0][c-1])
    
    tpos = (r*c+1)//2

    while mn<mx:
        mid = (mn+mx)//2
        midPos = 0

        for i in range(r):
            midPos+=bisect(arr[i],mid) # what this bisect do is it returns the number of elements which are less than or equal to mid
        
        if midPos<tpos:
            mn = mid+1
        else:
            mx=mid
    
    return mn
        



arr = [[5, 10, 20, 30, 40],
    [1, 2, 3, 4, 6],
    [11, 13, 15, 17, 19]]
print(printMedian(arr))