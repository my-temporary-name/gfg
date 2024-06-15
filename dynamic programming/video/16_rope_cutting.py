# rope cutting problem
# Given a rope of length n meters with three values a,b,c. We need to cut the rope in such a way that the cut pieces have length in a,b,c. 
# The task is to find the maximum number of pieces that can be made. 
# Eg: n=5, a=2, b=5, c=1 , 0<a,b,c<=n
# Output: 5 (cut the rope into pieces of length 1,1,1,1,1)

def maxPieces(n,a,b,c):
    if n==0:
        return 0
    if n<=-1:
        return -1
    res = max( maxPieces(n-a,a,b,c),
               maxPieces(n-b,a,b,c),
               maxPieces(n-c,a,b,c)
               )
    if res == -1:
        return -1
    return res+1

n = 5
a = 2
b = 5
c = 1
print(maxPieces(n,a,b,c)) # 5
print(maxPieces(9,2,2,2)) # -1