# find the maximum difference between two elements in an array; arr[j]-arr[i] : j>i

# Naive Approach: Time complexity: O(n^2)

def maxdiff(l):
    n = len(l)
    res = l[1]-l[0]
    for i in range(0,n-1):
        for j in range(i+1,n):
            res = max(res, l[j]-l[i])
    return res


l = [2,3,10,6,4,8,1]
print("Using 2 for loops: ",maxdiff(l))

# Efficient Approach: Time complexity: O(n)

l = [2,3,10,6,4,8,1]
n =len(l)

res = l[1]-l[0]
minval =l[0]

for i in range(1,n):
    res = max(res, l[i]-minval)
    minval = min(minval, l[i])

print("Using 1 for loop: ",res)