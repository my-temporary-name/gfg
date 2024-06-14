# Longest Common Subsequence
# Given two strings, find the length of the longest common subsequence
# Example: "ABCDGH" and "AEDFHR" => "ADH" => 3
# Subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.

# Method 1: Recursion, TC: O(2^n)

def lcs(s1, s2, n, m):
    if m==0 or n==0:
        return 0
    
    if s1[n-1] == s2[m-1]:
        return 1+lcs(s1, s2, n-1, m-1)
    
    else:
        return max(lcs(s1, s2, n-1, m), lcs(s1, s2, n, m-1)) # we are not decreasing both n and m, because we are looking for common subsequence not substring

s1 = "ABCDGH"
s2 = "AEDFHR"

print(lcs(s1, s2, len(s1), len(s2))) # 3

# Method 2: Memoization , TC: O(n*m)

M = 1000
N = 1000

memo = [[-1]*N for i in range(M)]

def lcs(s1,s2,n,m):
    if memo[n][m]!= -1:
        return memo[n][m]
    
    if n==0 or m==0:
        memo[n][m]=0
    
    else:
        if s1[n-1] == s2[m-1]:
            memo[n][m] = 1 + lcs(s1,s2,n-1,m-1)
        else:
            memo[n][m] = max(lcs(s1, s2, n-1, m), lcs(s1, s2, n, m-1))
    return memo[n][m]

s1 = "ABCDGH"
s2 = "AEDFHR"
print(lcs(s1, s2, len(s1), len(s2))) # 3

# Method 3: Tabulation, TC: O(n*m)

def lcs(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif s1[i-1]==s2[j-1]:
                dp[i][j]= 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

s1 = "ABCDGH"
s2 = "AEDFHR"
print(lcs(s1, s2)) # 3


# Variation: Print the longest common subsequence
# 1. Diff Utility (what lines are different in two files)
# 2. Minimum insertions and deletions to convert string a to string b
# 3. Shortest Common Supersequence (SCS) => "AGGTAB" and "GXTXAYB" => "AGXGTXAYB" => 9
# 4. Longest Palindromic Subsequence (LPS) => "BBABCBCAB" => "BABCBAB" => 7
# 5. Longest Repeated Subsequence (LRS) => "AABEBCDD" => "ABD" => 3
# 6. Space Optimized DP solution for LCS
# 7. Printing Longest Common Subsequence
