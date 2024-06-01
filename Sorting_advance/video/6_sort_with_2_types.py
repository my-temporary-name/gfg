# Sort an array with two types of elements

# 1. Segregate positive and negative numbers
# I/P: [15,-3,-2,18] O/P: [-3,-2,15,18]

# 2. Segregate even and odd numbers
# I/P: [15,14,13,12] O/P: [14,12,15,13] # this is not sorting but segregating

# 3. Sort a Binary Array
# I/P: [1,0,1,0,1] O/P: [0,0,1,1,1]

# Naive approach: TC = O(n) SC = O(n)

def sort_two(arr):
    n=len(arr)
    temp=[0]*n

    i=0

    for j in range(0,n):
        if arr[j]<0:
            temp[i] = arr[j]
            i+=1
    for j in range(0,n):
        if arr[j]>=0:
            temp[i]=arr[j]
            i+=1
    arr[:]= temp
    return arr

arr = [15,-3,-2,18]
print(sort_two(arr)) # [-3,-2,15,18]


# Efficient approach: TC = O(n) SC = O(1)

def sort_two2(arr):
    i,j=-1,len(arr)
    while True:
        i+=1
        while arr[i]<0:
            i+=1
        j-=1
        while arr[j]>=0:
            j-=1
        
        if i>=j:
            return
        arr[i],arr[j] = arr[j],arr[i]
    
arr = [15,-3,-2,18]
sort_two2(arr)
print(arr) # [-3,-2,15,18]
        