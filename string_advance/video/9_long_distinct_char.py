# Longest string with distinct characters
# Example: "geeksforgeeks" --> "eksforg" (7)

# Naive Approach: TC: O(n**3)
def areDistinct(str, i, j):

    # Note : Default values in visited are false
    visited = [0] * (256)

    for k in range(i, j + 1):
        if (visited[ord(str[k])] == True):
            return False

        visited[ord(str[k])] = True

    return True

# Returns length of the longest substring
# with all distinct characters.


def longestUniqueSubsttr(str):

    n = len(str)

    # Result
    res = 0

    for i in range(n):
        for j in range(i, n):
            if (areDistinct(str, i, j)):
                res = max(res, j - i + 1)

    return res
    return res

str = "geeksforgeeks"
print(longestUniqueSubsttr(str))


# Better Solution: TC: O(n**2)


def longDist(s):
    n = len(s)
    res = 0
    for i in range(n):
        visited = [0]*256
        for j in range(i,n):
            if visited[ord(str[j])] ==True:
                break
            else:
                res = max(res, j-i+1)
                visited[ord(str[j])] = True
    return res

str = "geeksforgeeks"
print(longDist(str))


# Efficient Solution: TC: O(n)

def LD(s):
    n = len(s)
    res  =0
    prev = [-1]*256 
    i =0
    for j in range(n):
        i = max(i, prev[ord(s[j])]+1)
        max_end = j-i+1
        res = max(res, max_end)
        prev[ord(str[j])] = j
    return res

str = "geeksforgeeks"
print(LD(str))