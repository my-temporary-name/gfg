# Dynamic Programming (tabulation) for Fibonacci Series: TC: O(n) Bottom Up approach
# Bottom Up approach

def fib(n):
    dp = [None] * (n+1)
    dp[0]=0
    dp[1]=1

    for i in range(2,n+1):
        dp[i]=dp[i-1] + dp[i-2]
    return dp[n]

print(fib(10)) # 55

# Here we have a linear array of sub problems, which are being solved only once, so we have optimized it using tabulation.
#                fib(5)
#              /        \
#          fib(4)       fib(3)
#         /      \
#     fib(3)      fib(2)
#     /    \
# fib(2)  fib(1)
# /    \
#fib(1) fib(0)
