# Sort an array with tree types of elements

# 1. Sort an array of 0s, 1s and 2s
# I/P: [0,1,2,0,1,2] O/P: [0,0,1,1,2,2]

# 2. Three way Partitioning
# I/P: [2,1,2,20,10,20,1], pivot=2 O/P: [1,1,2,2,20,20,10] # all elements less than 2 should come first, then 2 and then greater than 2

# 3. Partition around a range
# I/P: [10,5,6,3,20,9,40], low=5, high=10 O/P: [3,5,6,9,10,20,40] # all elements less than 5 should come first, then 5 to 10 and then greater than 10


# Naive solution: TC = O(n) SC = O(n)   
# first copy all 0s to temp array, then copy all 1s and then 2s

def Sort_arr(arr):
    temp = []
    for x in arr:
        if x==0:
            temp.append(x)
    
    for x in arr:
        if x==1:
            temp.append(x)
    
    for x in arr:
        if x==2:
            temp.append(x)
    
    arr[:]=temp
    return arr

arr = [0,1,2,0,1,2,2,1]
print(Sort_arr(arr)) # [0,0,1,1,2,2]

# Efficient solution: DUTCH NATIONAL FLAG ALGORITHM TC = O(n) SC = O(1)
# maintain 4 sections: 0 to low-1, low to mid-1, mid to high, high+1 to n-1

def sort_arr(arr):
    low,mid,high = 0,0,len(arr)-1
    while mid<=high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            high-=1
    return arr

arr = [0,1,2,0,1,2,2,1]
print(sort_arr(arr)) # [0,0,1,1,2,2]