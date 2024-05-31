# Naive approach for pattern searching: TC = O((n-m+1)*m)

def naivePat(txt,pat):
    m = len(pat)
    n = len(txt)

    for i in range(n-m+1):
        j = 0
        while j<m:
            if pat[j]!=txt[i+j]:
                break
            j+=1
        if j==m:
            print(i,end=" ")

txt = "GEEKSFORGEEKS"
pat = "EKS"
naivePat(txt,pat)

# Improved version of naive pattern searching for distinct characters in pattern
# If we see a mismatch after j matches then we increment i by j


def impNaivePat(txt,pat):
    n = len(txt)
    m = len(pat)

    i = 0
    while i<=(n-m):
        for j in range(m):
            if pat[j]!=txt[i+j]:
                break
            j+=1
        
        if j==m:
            print(i, end=" ")
            i+=m
        if j==0:
            i+=1
        else:
            i+=j

txt = "ABCEABFABCD"
pat = "ABCD"
impNaivePat(txt,pat)