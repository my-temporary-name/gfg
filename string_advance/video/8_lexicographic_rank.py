# Lexicographic rank of a string
# Given a string, find its rank among all its permutations sorted lexicographically. For example, rank of “abc” is 1, rank of “acb” is 2, and rank of “cba” is 6.
# Permutations of "abc" are: abc, acb, bac, bca, cab, cba

# generate all permutations of a string in increasing order i.e lexicographically sorted


# Efficient solution:
# Count lexicographically smaller strings + 1

# "DCBA"

# A  _ _ _ , B _ _ _, C _ _ _ (a,b,c  are smaller than D) 3 x 3! = 18
# DC_ _, DA_ _ (a,b are smaller than C) 2 x 2! = 4
# DCA _ (a is smaller than B) 1 x 1! = 1

# Total = 18+4+1 = 23 --> rank = 24

CHAR = 256

def fact(n):
      
    if n == 0:
        return 1
     
    return n * fact(n-1)

def lexRank(s):
    res =1
    n = len(s)
    mul = fact(n)
    count = [0]*CHAR
    for i in range(n):
        count[ord(str[i])]+=1
    for i in range(1,CHAR):
        count[i]+=count[i-1]
    for i in range(n-1):
        mul = mul//(n-i)
        res += count[ord(str[i])-1]*mul
        for j in range(ord(str[i]),CHAR):
            count[j]-=1
    return res

str = "string"
print(lexRank(str))
