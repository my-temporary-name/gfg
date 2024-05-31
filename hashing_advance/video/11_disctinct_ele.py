# Count distinct elements in every window
 
# arr = [10,20,20,10,30,40,10], k =4, output = 2,3,4,3
# Naive solution: TC=O((n-k+1)*k)

# 1. There will be n-k+1 windows
# 2. Traverse through every window and count distinct elements in it.


def disct(arr,k):
    n = len(arr)
    for i in range(n-k+1):
        print(len(set(arr[i:i+k])),end=" ")


arr = [10,20,20,10,30,40,10]
k = 4
disct(arr,k)

print("\n\n\n")


# Efficient solution: TC = O(n)
# The idea is to use count of previous window to get the current count
from collections import Counter
def disct2(arr,k):
    n = len(arr)
    # Let's see first window
    mp = Counter(arr[0:k])
    print(len(mp),end=" ")

    for i in range(k,len(arr)):
        # remove first item from prev window
        x = arr[i-k]
        mp[x]-=1
        mp[arr[i]]+=1
        if mp[x]==0:
            del mp[x]
        print(len(mp),end=" ")



arr = [10,20,20,10,30,40,10]
k = 4
disct2(arr,k)