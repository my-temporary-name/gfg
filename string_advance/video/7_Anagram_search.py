# Anagram Search
# We are given a big string and a small string. We need to find all the anagrams of the small string in the big string.
# Anagram: Two strings are anagrams of each other if one string can be formed by rearranging the characters of the other string.

# Example: big = "geeksforgeeks" small = "egek" --> 2 (geek, egek)

# Naive solution: TC = O((n-m+1)*m)
CHAR=256

def areAnagram(pat, txt,i):
    count = [0]*CHAR

    for j in range(len(pat)):
        count[ord(pat[j])]+=1
        count[ord(txt[i+j])]-=1
    for j in range(CHAR):
        if count[j]!=0:
            return False
    return True

def isPresent(txt,pat):
    n = len(txt)
    m = len(pat)
    for i in range(n-m+1):
        if areAnagram(pat,txt,i):
            return True
    return False

txt = "geeksforgeeks"
pat = "frog"
print(isPresent(txt,pat))

# Efficient solution: TC = O(m+(n-m)xCHAR) --> O(n x CHAR)
# we'll use sliding window technique add remove the characters from the window and check if the count of characters in the window is same as the count of characters in the pattern

# Anagram Search

CHAR = 256
def aresame(ct,cp) :
    for i in range(CHAR) :
        if ct[i] != cp[i] :
            return False
    return True
    
def ispresent(txt,pat) :
    n = len(txt) 
    m = len(pat)
    ct = [0] * CHAR
    cp = [0] * CHAR
    for i in range(m) :
        ct[ord(txt[i])] += 1 
        cp[ord(pat[i])] += 1 
    for i in range(m,n) :
        if aresame(ct,cp) :
            return True
        ct[ord(txt[i])] += 1 
        ct[ord(txt[i-m])] -= 1
    return False
    
    
txt = "geeksforgeeks"
pat = "frog"
print(ispresent(txt,pat))