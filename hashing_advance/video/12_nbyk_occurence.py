# More than n/k occurrences

# Given an array of size n and a number k, find all elements that appear more than n/k times
# example: arr = [30,10,20,20,10,20,30,30], k=4, output = 20,30 (n/k = 8/4 = 2)

# Naive solution: TC= O(nlogn)
# 1. Sort the given arr. 2. Traverse through the arr and count the frequency of each element. 3. If frequency > n/k, print the element

def printNbyK(arr,k):
    arr.sort()
    i = 1 # we don't include 0th element
    count =1
    while(i<len(arr)):
        while i<len(arr) and arr[i]==arr[i-1] : # logn time
            count+=1
            i+=1
        if count > len(arr)//k:
            print( arr[i-1],end=" ")
        count=1
        i+=1 # again we don't include the current element

arr = [30,10,20,20,10,20,30,30]
k = 4
printNbyK(arr,k)

# Or directly we can use Counter from collections

from collections import Counter

def printNbyK2(arr,k):
    mp = Counter(arr)
    n = len(arr)
    for x in mp:
        if mp[x]>n//k:
            print(x,end=" ")

arr = [30,10,20,20,10,20,30,30]
k = 4
printNbyK(arr,k)

# More Efficient solution: TC= O(nk)

def printNbyK3(arr,k):
    n = len(arr)
    mp = {}
    for i in range(n):
        if arr[i] in mp:
            mp[arr[i]]+=1
        elif len(mp)<k-1:
            mp[arr[i]]=1
        else:
            for x in mp:
                mp[x]-=1
                if mp[x]==0:
                    del mp[x]
    for x in mp:
        mp[x]=0
    for i in range(n):
        if arr[i] in mp:
            mp[arr[i]]+=1
    for x in mp:
        if mp[x]>n//k:
            print(x,end=" ")

arr = [30,10,20,20,10,20,30,30]
k = 4
printNbyK3(arr,k)