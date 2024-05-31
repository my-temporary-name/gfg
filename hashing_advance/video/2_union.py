# Union of Two unsorted Arrays
# Example: a = [1, 3, 5, 7], b = [0, 2, 6, 8, 9]; Output: [0, 1, 2, 3, 5, 6, 7, 8, 9]

# Naive Approach:

def unnion(arr1,m,arr2,n):
    c = [0]*(m+n)
    for i in range(m):
        c[i] = arr1[i]
    
    for i in range(n):
        c[m+i] = arr2[i]
    
    res = 0
    for i in range(m+n):
        flag = False
        for j in range(i):
            if c[i]==c[j]:
                flag = True
                break
        if flag ==False:
            res+=1
    return res


arr1 = [1, 3, 5, 7]
arr2 = [0, 2, 6, 8, 9,5,7,11]
print(unnion(arr1, len(arr1), arr2, len(arr2)))


# Efficient Approach: TC = O(m+n), SC= O(m+n)

def unnion2(arr1,m,arr2,n):
    us=set()
    for i in arr1:
        us.add(i)
    for i in arr2:
        us.add(i)
    return len(us)



arr1 = [1, 3, 5, 7]
arr2 = [0, 2, 6, 8, 9,5,7,11]
print(unnion2(arr1, len(arr1), arr2, len(arr2)))

