# Palindrome Partitioning
# Given a string, a partitioning of the string is a palindrome partitioning if every substring of the partition is a palindrome. 
# Determine the fewest cuts needed for a palindrome partitioning of a given string.

# Eg: geeks -> 2 cuts i.e g|ee|ks so ee is a palindrome
# Eg: nitin -> 0 cuts as nitin is a palindrome
# Eg: abbac -> 1 cut i.e abba|c so abba is a palindrome
# Eg: abcde -> 4 cuts i.e a|b|c|d|e so each character is a palindrome


# Recursive approach: TC: O(2^n)
def isPalindrome(s, i, j): # check if the string is palindrome
    while(i<j):
        if(s[i]!=s[j]):
            return False
        i+=1 
        j-=1 
    return True
    

def palPart(s, i ,j):
    if(isPalindrome(s, i, j)): # if the string is palindrome, then no cuts are needed
        return 0
    res= float('inf')
    for k in range(i, j):
        res=min(res, 1+palPart(s, i, k)+palPart(s, k+1, j)) # make a cut at k and check for the left and right part
    
    return res
    
s="geek"
print(palPart(s, 0, len(s)-1))

# Method 2: Recursion + Memoization TC: O(n^2)
def isPalindrome(s, i, j):
    while(i<j):
        if(s[i]!=s[j]):
            return False
        i+=1 
        j-=1 
    return True
    

def palPart(s):
    n=len(s)
    dp=[[0 for x in range(n)] for x in range(n)] # dp[i][j] will store the minimum number of cuts needed for the string s[i:j+1]
    
    for gap in range(n): # gap will be the difference between i and j
        for i in range(n-gap): # i will be the starting index and j will be the ending index
            j=i+gap 
            if(isPalindrome(s,i,j)):
                dp[i][j]=0
            else:
                dp[i][j]=float('inf')
                for k in range(i, j):
                    dp[i][j]=min(dp[i][j], 1+dp[i][k]+dp[k+1][j]) # make a cut at k and check for the left and right part
    return dp[0][n-1]
    
    
s="geek"
print(palPart(s))
