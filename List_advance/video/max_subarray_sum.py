# find maximum subarray sum, subarray are contiguous elements of the array.

# Example: [2,3,-8,7,-1,2,3] => 11 i.e 7+(-1)+2+3

# Naive Approach: Time complexity: O(n^2)

l = [2,3,-8,7,-1,2,3]
res =l[0]
n = len(l)

for i in range(0,n):
    curr=0
    for j in range(i,n):
        curr = curr + l[j]
        res = max(res, curr)
    
print("Using 2 for loops: ",res)

# Efficient Approach: Time complexity: O(n)
# MaxEnding(i) = max( MaxEnding(i-1)+arr[i], arr[i])

l = [2,3,-8,7,-1,2,3]
n =len(l)
res =l[0]
maxEnding = l[0]

for i in range(1,n):
    maxEnding = max(maxEnding+ l[i], l[i])
    res = max(maxEnding, res)

print("Using 1 for loop: ",res)