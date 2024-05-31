# Minimum Consecutive Flips to make all 1s or 0s
# Example: [1,1,0,0,0,1] ; Output: 2 to 4

# Idea will be we will start flipping from second group
# Example: [1,1,0,0,0,1] ; Output: 2 to 4 # Second group is 0,0,0

def printGroups(arr,n):
    for i in range(1,n): # we will start from 1
        if arr[i]!=arr[i-1]:
            if arr[i]!=arr[0]:
                print("From ",i," to ",end=" " )
            else:
                print(i-1)
    if arr[n-1]!=arr[0]:
        print(n-1)

arr= [0,0,1,1,0,0,1,1,0,1,1,1]
printGroups(arr,len(arr))