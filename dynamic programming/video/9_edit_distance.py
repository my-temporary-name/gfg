# Edit Distance Problem
# In the edit distance problem we are given two strings and our goal is to convert one string into another using the minimum number of operations. 
# The operations we can perform are: insert, delete , replace.
# Eg: s1: "Saturday", s2: "Sunday"
# Output: 3 (convert "Saturday" to "Sunday" using 3 operations) i.e. delete 'a', 't' and replace 'r' with 'n'


# Method 1: Recursion, Time Complexity: O(3^n) because at each step we have 3 choices

def eD(s1, s2, m, n):
    if m==0:
        return n
    if n==0:
        return m
    
    if s1[m-1] == s2[n-1]: # if last characters are same
        return eD(s1,s2,m-1,n-1) # ignore last characters and recur for remaining strings
    else:
        return 1 + min(eD(s1,s2,m,n-1), # insert
                       eD(s1,s2,m-1,n), # delete
                       eD(s1,s2,m-1,n-1) # replace
                        )

s1 = "Saturday"
s2 = "Sunday"
print(eD(s1,s2,len(s1),len(s2))) # 3

# Method 2: Recursion + Memoization, Time Complexity: O(m*n)

def ed2(s1, s2, m, n):
    dp = [[0]*(n+1) for i in range(m+1)] # create a 2D array to store the results of subproblems

    # if first string is empty, insert all characters of second string
    for i in range(m+1):
        dp[i][0] = i
    # if second string is empty, remove all characters of first string
    for j in range(n+1):
        dp[0][j] = j
    
    # fill the dp array in bottom-up fashion
    for i in range(1,m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]: # if last characters are same
                dp[i][j] = dp[i-1][j-1] # ignore last characters and recur for remaining strings
            else:
                dp[i][j] = 1 + min(dp[i][j-1], # insert
                                dp[i-1][j], # delete
                                dp[i-1][j-1] # replace
                                )
    return dp[m][n]

s1 = "Saturday"
s2 = "Sunday"
print(ed2(s1,s2,len(s1),len(s2))) # 3