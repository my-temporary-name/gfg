# We are given a rope of length n, we need to find the maximum number of pieces we can make such that the length of every piece is in set {a,b,c}
# We can cut the rope in any way we want, we just need to maximize the number of pieces.
# Example: n=5, a=2, b=5, c=1 : 5=5, 5=2+2+1, 5=2+1+1+1, 5=1+1+1+1+1, 5=1+2+2 ; So, the maximum number of pieces we can make is 5 of length 1.

# Idea: Using recursion, We can make cut of either a, b or c length. So, we will make cut of a length and then recursively call for remaining length.
# Base case will be when n=0, we can't make any more cut. So, return 0. -ve case will be when n<0, we can't make cut of -ve length. So, return -1. 

def maxPieces(n, a,b,c): # Time complexity: O(3^n) in worst case when a,b,c all are 1
    if n==0: # When we can't make any more cut
        return 0
    if n<=-1: # when we can't make cut of -ve length
        return -1
    res = max(maxPieces(n-a, a,b,c),
              maxPieces(n-b,a,b,c),
              maxPieces(n-c, a,b,c))
    
    if res == -1: # In case we can't make cut of a,b,c length eg, n =5, a=2, b=2, c=2
        return -1
    return res +1

n = 23
a = 11
b = 9
c = 12

print(maxPieces(n,a,b,c)) # 2