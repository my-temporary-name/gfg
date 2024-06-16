# Allocate minimum number of pages
# Given number of pages in n different books and m students. 
# The books are arranged in ascending order of number of pages. 
# Every student is assigned to read some consecutive books. 
# The task is to assign books in such a way that the maximum number of pages assigned to a student is minimum.

# Eg: [10,20,30,40], m=2
# O/p: 60 # 10+20+30, 40

# Eg: [10,5,30,1,2,5,10,10], m=3
# O/p: 30 # 1st student: 10+5=15, 2nd student: 30, 3rd student: 1+2+5+10+10=28


# Recursive approach: TC: O(2^n)
# Idea: We have m students and n books. We have to divide the books among m students such that the maximum number of pages assigned to a student is minimum.
# We have two choices for each student, either assign the current book to the current student or start a new student.

# Allocate Minimum Pages (Naive Method)


def minpages(arr,n,k) :
    if (k == 1) : # if only one student, then he has to read all the books
        return sum(arr[0:n])
    if (n == 1) : # if only one book, then he has to read that book
        return arr[0]
    res = float('inf')
    for i in range(1,n) :
        res = min(res,max(minpages(arr,i,k-1),sum(arr[i:n]))) # either assign the current book to the current student or start a new student
    return res
    
    
arr = [10,5,30,1,2,5,10,10]
n = len(arr)
k = 3 
print(minpages(arr,n,k))

# Dynamic Programming approach: TC: O(n^2 * k)
# Idea: We have m students and n books. We have to divide the books among m students such that the maximum number of pages assigned to a student is minimum.
# We have two choices for each student, either assign the current book to the current student or start a new student.


def minPages(arr,n,k):
    dp = [[None]*(n+1)]*(k+1) # dp[i][j] will store the minimum number of pages that can be assigned to i students from j books
    for i in range(1,n+1):
        dp[1][i] = sum(arr[0:i])
    
    for i in range(1,k+1):
        dp[i][1] = arr[0]
    
    for i in range(2, k+1):
        for j in range(2, n+1):
            res = float('inf')
            for p in range(1,j):
                res = min(res,max(dp[i-1][p],sum(arr[p:j]))) # either assign the current book to the current student or start a new student
            dp[i][j] = res
    return dp[k][n]

arr = [10,5,30,1,2,5,10,10]
n = len(arr)
k = 3
print(minPages(arr,n,k)) # 30