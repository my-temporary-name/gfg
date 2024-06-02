# Cycle Sort

# 1. A worst case O(n^2) time complexity sorting algorithm.
# 2. In-place, not stable.
# 3. Does minimum memory writes and can be useful when memory write operation is costly.
# 4. Can be useful to solve problems like find minimum swaps required to sort an array.

def CycleSort(arr):
    w=0
    for cs in range(len(arr)-1):
        item = arr[cs]
        pos = cs
        for i in range(cs+1, len(arr)): # find the pos of the cycle start element.
            if arr[i]<item:
                pos+=1
        if pos==cs:
            continue
        arr[pos],item = item, arr[pos] # put item as correct position.
        w+=1

        while item == arr[pos]:
            pos += 1
        arr[pos], item = item, arr[pos]
        w += 1

        while pos!= cs: # Fix all the elements of the cycle starting with the item.
            pos = cs
            for i in range(cs+1, len(arr)):
                if arr[i]<item:
                    pos = pos+1
            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]
            w += 1
    
    return arr

arr = [20,40,50,10,30]
print(CycleSort(arr)) # [1,2,3,4,5]
