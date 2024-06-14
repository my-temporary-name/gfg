# Dynamic Programming: Introduction 
# In simple words, it is an optimization over plain recursion.
# The idea is to simply store the results of sub problems, so that we do not have to re-compute them when needed later.
# 1. Memoization (Top Down): The memoized program for a problem is similar to the recursive version with a small modification that it looks into a lookup table before computing solutions.
# 2. Tabulation (Bottom Up): The tabulated program for a given problem builds a table in bottom up fashion and returns the last entry from table.

# Application of Dynamic Programming:
# 1. Bellman-Ford Algorithm
# 2. Floyd-Warshall Algorithm
# 3. Diff Utility (LCS)
# 4. Search closed words in a dictionary (Edit Distance)
# 5. Resource allocation
# ... and many more


# Dynamic Programming (memoization) for Fibonacci Series:

# First let's see linear time complexity solution using recursion, TC: O(2^n)

def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10)) # 55

# Here we have a tree of sub problems, which are being solved multiple times, so we can optimize it using memoization.
#                fib(5)
#              /        \
#          fib(4)       fib(3)
#         /      \      /    \
#     fib(3)    fib(2) fib(2) fib(1)
#     /    \     /   \   /   \  /   \      
# fib(2)  fib(1) .... .... .... .... 
# /    \
#fib(1) fib(0)




# Now let's see the optimized solution using memoization, TC: O(n) Top Down approach

memo = [None]*100 # global array to store the results of sub problems assuming n<=100

def fib(n):
    if memo[n]!=None:
        return memo[n]
    if n==0 or n==1:
        memo[n]=n
    else:
        memo[n] = fib(n-1 ) + fib(n-2)
    return memo[n]

print("\n",fib(10)) # 55
# Here we have a tree of sub problems, which are being solved only once, so we have optimized it using memoization.
#                fib(5)
#              /        \
#          fib(4)       fib(3)
#         /      \    
#     fib(3)      fib(2)
#     /    \       
# fib(2)  fib(1)
# /    \
#fib(1) fib(0)
