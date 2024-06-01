# Construct Longest Proper prefix suffix array : find a string which is both prefix and suffix of the given string

# Proper prefix: "abc"" -> "", "a", "ab", "abc"
# Proper suffix: "abc" -> "", "c", "bc", "abc"

# str= "abacabad"
# lps = [0,0,1,0,1,2,3]
# [0: no proper prefix and suffix, 0: no proper prefix and suffix, 1: a, 0: no proper prefix and suffix, 1: a, 2: ab, 3: aba, 0: no proper prefix and suffix]

# str= "abbabb"
lps = [0,0,0,1,2,3]

# Naive solution= TC: (n**3)

def LongProperPS(str,n):
    for len in range(n-1, -1, -1):
        for j in range(len):
            if str[j]!= str[n-len+j]:
                break
        else:
            return len
    return 0


def FillLPS(str):
    lps = [0]*len(str)
    lps[0]=0

    for i in range(1,len(str)):
        lps[i] = LongProperPS(str,i+1)

str = "ababacab"

print(FillLPS(str))


# Effecient Solution: TC: O(n)

# Idea: 1. if len = lps[i-1] and str[len] and str[i] are same, then lps[i]= len+1
# 2. if str[i] and str[len] are not same:
#   a. if len ==0, lps[i]=0
#   b. Else, we recursively apply lps[], len=lps[len-1] and then compare str[i] and str[len]

def FillLPS(s):
    lps = [0]*len(s)
    lps[0]=0

    i = 1
    l = 0
    n = len(s)
    while(i<n):
        if s[i]==s[l]:
            l+=1
            lps[i]=l
            i+=1
        else:
            if l ==0:
                lps[i]=0
                i+=1
            else:
                l = lps[l-1]
    return lps

s = "ababacab"

print(FillLPS(s))
    