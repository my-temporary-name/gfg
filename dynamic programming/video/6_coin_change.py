# Coin change problem
# Given a set of coins and a target value, your task is to find number of ways to make the target value using the coins.

# Example: coins = [1,2,3], target = 4
# Output: 4 => {1,1,1,1}, {1,1,2}, {2,2}, {1,3}

# Idea for the recursive solution:
# we have two choices for each coin, either we include it or exclude it.
# if we include it, we will have the same target value and we will have all the coins available.
# if we exclude it, we will have the same target value and we will have all the coins except the current coin.

def count_ways(coins, n, s):
    if s==0:
        return 1
    if s<0:
        return 0
    if n==0:
        return 0
    return count_ways(coins,n,s-coins[n-1]) + count_ways(coins,n-1,s)

coins = [1,2,3]
target = 4
print(count_ways(coins, len(coins), target)) # 4

# Method 2: Using DP, TC: O(n*m)
# dp[i][j] = number of ways to make the target value j using the first i coins
# dp[i][j] is 1 if s==0
# dp[i][j] is 0 if s>0 and n==0
# dp[i-1][j] if coin[i-1] > j
# dp[i-1][j] + dp[i][j-coins[i-1]] in all other cases


def count_ways(coin,s):
    n = len(coin)
    dp = [[0 for x in range(s+1)] for i in range(n+1)]

    for i in range(n+1):
        dp[i][0]=1
    for i in range(1, n+1):
        for j in range(1, s+1):
            dp[i][j] = dp[i-1][j]
            if j>=coin[i-1]:
                dp[i][j] += dp[i][j-coin[i-1]]
    return dp[n][s]

coins = [1,2,3]
target = 4
print(count_ways(coins, target)) # 4
