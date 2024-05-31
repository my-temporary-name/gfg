# Find maximum amount of water that can be trapped within the given set of bars.
# Example: [3,0,1,2,5] => 3

# If array is in increasing or decreasing order, then we can't trap any water.

# Naive Approach: Time complexity: O(n^2)

def getWater(l,n):
    res =0
    for i in range(1,n-1):
        left_max = l[i]

        for j in range(0,i):
            left_max = max(left_max, l[j])
        
        right_max=l[j]
        for j in range(i+1, n):
            right_max = max(right_max, l[j])
        
        res = res+(min(left_max, right_max) - l[i])
    
    return res

l = [3,0,1,2,5]
n = len(l)
print("Using 2 for loops: ",getWater(l,n))

# Efficient Approach: Time complexity: O(n) , Find left max and right max for each element and then find the trapped water.

def getWater(l,n):
    res =0
    lmax = [0]*n
    rmax = [0]*n

    lmax[0] = l[0]
    for i in range(1,n):
        lmax[i] = max(l[i],lmax[i-1])
    
    rmax[n-1]=l[n-1]
    for i in range(n-2,-1,-1):
        rmax[i] = max(l[i], rmax[i+1])

    for i in range(1, n-1):
        res = res + (min(lmax[i],rmax[i]) - l[i])
    
    return res

l = [3,0,1,2,5]
n = len(l)
print("Using 1 for loop: ",getWater(l,n))