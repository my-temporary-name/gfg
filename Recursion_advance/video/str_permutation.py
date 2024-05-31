# Print all the permutations of the given string.
# Example: s = "abc" ; Output: ["abc", "acb", "bac", "bca", "cab", "cba"]

def permute(s,i):
    n = len(s)
    if  i==n-1:
        print("".join(s))
        return
    for j in range(i,n):
        s[i],s[j] = s[j],s[i]
        permute(s,i+1)
        s[i],s[j] = s[j],s[i]

print(permute(list("abc"),0)) # abc acb bac bca cba cab None
