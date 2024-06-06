# ceiling on the left side array
# I/p: [2, 8, 30, 15, 25, 12]
# O/p: [-1, -1, -1, 30, 30, 15]
# Ceil value of an element is the smallest element greater than or equal to the element
# first element will always have -1 as there is no element on the left side of it

# Naive Approach: TC= O(n^2), SC= O(1)

import sys

def printCeil(arr):
    n = len(arr)
    print("-1", end= " ")

    for i in range(1,n):
        diff = sys.maxsize # max value of integer

        for j in range(i):
            if arr[j]>=arr[i]:
                diff = min(diff, arr[j]-arr[i])
        
        if diff == sys.maxsize:
            print("-1", end= " ")
        else:
            print(arr[i]+diff, end= " ")

arr = [2, 8, 30, 15, 25, 12]
printCeil(arr)


# Efficient Approach: TC= O(n), SC= O(n) 
# Idea is to use self balancing BST


def printCeil2(arr):
    n = len(arr)
    print("-1", end= " ")

    s= set()
    s.add(arr[0])

    for i in range(1,n):
        it = [x for x in s if x>=arr[i]]

        if len(it)==0:
            print("-1", end= " ")
        
        else:
            print(min(it), end = " ")
        s.add(arr[i])

arr = [2, 8, 30, 15, 25, 12]
printCeil2(arr)