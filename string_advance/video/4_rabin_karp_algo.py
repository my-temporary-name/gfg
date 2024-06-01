# Rabin karp string matching algorithm

# 1. Like naive algo, slide the pattern one by one
# 2. Compare the hash values of pattern and current text window
# If the hash values match then only compare the characters one by one.
# this way we can avoid comparing all characters of the pattern.

# Example: txt = " abdabcbabc", pat = "abc"
# hash value :  a:!, b:2, c:3, d:4, e:5
# hash value of "abc" = 1+2+3 = 6

# i =0, hash value of text window = 1+2+4 = 7 != 6
# i =1, hash value of text window = 2+4+1 = 7 != 6
#... So on
# If hash values match then only compare the characters one by one

# ----------------------------------------------------------
# Let's see improved hash function for Rabin Karp algo
# d= 5 (a:1, b:2, c:3, d:4, e:5)
# h(abc) = 1xd**2 + 2xd**1 + 3xd**0 = 1x5**2 + 2x5**1 + 3x5**0 = 1x25 + 2x5 + 3x1 = 25+10+3 = 38
# h(dab) = 4x5**2 + 1x5**1 + 2x5**0 = 4x25 + 1x5 + 2x1 = 100+5+2 = 107

# Rolling hash function:
# t i+1 = d(t i - txt[i]) X d**(m-1) + txt[i+m] // m is length of pattern

# Example: txt = "132456" d=10 m = 4
# t0 = 1324
# t1 = (1324 - 1x10**3) X 10 + 5 = 3245


d = 256 # No of characters in the input alphabet
def RKsearch(pat, txt, q): # q is a prime number which is used to avoid overflow of hash values
    m, n = len(pat), len(txt)
    h=1

    for i in range(1,m):
        h = (h*d)%q # we need h to calculate hash value of next window ( (d** (m-1))%q)
    p,t =0,0
    for i in range(m): # to compute hash value of pattern and first window of text
        p = (p*d*ord(pat[i]))%q
        t = (t*d*ord(txt[i]))%q
    
    #check for spurious hits
    for i in range(n-m+1):
        if p==t:
            for j in range(m):
                if txt[i+j]!=pat[j]:
                    break
            else: # if j loop completes without break
                print(i, end = " ") 
        if i< (n-m): # compute t i+1 using ti
            t= ((d*(t-ord(txt[i])*h))+ ord(txt[i+m]))%q
        if t<0:
            t=t+q

txt = "GEES FOR GEEKS"
pat = "GEEK"
q = 101
RKsearch(pat, txt, q)

# time complexity of Rabin Karp algo in worst case is O((n-m+1)*m) but in average case it is O(n+m)