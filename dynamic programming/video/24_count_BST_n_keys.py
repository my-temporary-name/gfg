# Count BSTs with n keys (binary search trees with n keys)
# Given an integer n, the task is to find the number of unique BSTs that can be created using n keys.
# Eg: n = 3
# Output: 5
#   1                1     and so on
#    \              / 
#     2           2
#      \           \
#       3           3


def countBST(n):
    dp = [0]*(n+1)
    dp[0]=1

    for i in range(1,n+1):
        for j in range(i):
            dp[i] += dp[j] * dp[i-j-1]
    return dp[n]

n = 3
print(countBST(n)) # 5
print(countBST(5)) # 14

# directly using formula, CATLAN NUMBER
# C(n) = (2n)! / (n+1)n!