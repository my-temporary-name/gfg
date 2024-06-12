# Back Tracking
# Given a string print all those permutations which does not contain "AB" as a substring.
# I/P: ABC
# O/P: ACB, BAC, BCA, CBA (excluding ABC, CAB)

# Naive approach: TC: O(n!) SC: O(n)

def permute(s, l, r): # l is left index, r is right index
    if l == r:
        if "AB" not in "".join(s):
            print(*s, sep="", end=" ")
        return
    else:
        for i in range(l, r+1):
            s[i], s[l] = s[l], s[i]
            permute(s,l+1,r)
            s[i], s[l] = s[l], s[i]

s = "ABC"
n = len(s)
permute(list(s), 0, n-1)

# Optimized approach: TC: < O(n! * n)
print()

def isSafe(s, l, i, r):
    if l!=0 and s[l-1] == "A" and s[i] == "B": # if the previous character is A and the current character is B
        return False
    if r == l+1 and s[i]=="A" and s[l]== "B": # if the current character is A and the previous character is B
        return False
    
    return True

def permute(s,l,r):
    if l==r:
        print(*s, sep="", end=" ")
        return

    else:
        for i in range(l, r+1):
            if isSafe(s, l, i ,r):
                s[i], s[l] = s[l], s[i]
                permute(s,l+1,r)
                s[i], s[l] = s[l], s[i]

s = "ABC"
permute(list(s), 0, len(s)-1)