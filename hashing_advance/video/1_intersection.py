# Intersection of Unsorted arrays!
# Return count of distinct common elements in these 2 arrays.

# Naive Solution: O(m x (m+n))
# 1. Initialize res =0
# 2. Traverse through every element of a[]
# 2.1 Check of it has not appeared already
# 2.2 If a new element and also present in b[], do res++
# 3. Return res


def intersection(arr1, m , arr2, n):
    res=0 
    for i in range(m):
        flag=False
        for j in range(i-1):
            if(arr1[j]==arr1[i]):
                flag=True
                break
        if(flag==True):
            continue
        for j in range(n):
            if(arr1[i]==arr2[j]):
                res+=1
                break
    return res 
    
m=8
n=2
arr1=[10, 15, 20, 15, 30, 30, 5, 80]
arr2=[30,80]
print(intersection(arr1, m, arr2, n))

# Efficient Solution 1: TC = O(m), SC= (n+m)
# 1. Insert all elements of a[] in set and same with b[]
# 2. Traverse through set a and increment for elements that are present in set b

# Efficient Solution 2: TC = O(m)
# 1. Insert all elements of a[] in a set
# 2. Traverse through b[]. Search for every element b[i] in set a and increment if found also remove b[i] from set a.

def intersection2(arr1,m,arr2,n):
    us = set()
    for i in range(m):
        us.add(arr1[i])
    res=0

    for i in range(n):
        if arr2[i] in us:
            res+=1
            us.remove(arr2[i])
    return res

arr1=[10, 15, 20, 15, 30, 30, 5, 80]
arr2=[30,80,30,3]

print( intersection2(arr1, len(arr1), arr2, len(arr2) ) )