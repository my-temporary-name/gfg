# Longest Common Subsequence: x, x+1, x+2, x+3, x+4, x+5 in any order
# arr = [1,9,3,4,2,20] ,ans 4 (1,3,4,2)

# naive solution: use sorting and find the longest subsequence ,TC = O(nlogn)
# arr.sort()
# run loop and check if arr[i] == arr[i-1]+1, if yes then increment the count


# Efficient solution: TC=O(n) because we are using hashing
# 1. We first insert all elements in a hash table
# 2. Then with 2n lookups we find the result

# arr = [1, 3, 4, 3, 3, 2, 9 ,10]
# ht= [1, 3,4,2,9,10]

def findlong(arr):
    s = set()
    res = 0
    for i in arr:
        s.add(i)
    for i in arr:
        if i-1 not in s:
            curr=1
            while curr+i in s: # we will look each element twice
                curr+=1
            res = max(res, curr)
    return res

arr = [1, 3, 4, 3, 3, 2, 9 ,10]
print(findlong(arr))