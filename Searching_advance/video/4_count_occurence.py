# Count occurrence of a number in a sorted array
# Example: [2,4,10,10,10,18,20], x=10; Output: 3

# Naive Solution: Time Complexity: O(n), Space Complexity: O(1) ; Using Linear Search

# Efficient Solution: Time Complexity: O(log(n))+O(k) [k is number of time element occurred ], Space Complexity: O(1) ; Using Binary Search
# We will do a binary search to get X element and the we will traverse left and right to get the count of X element

# More Efficient Solution: Time Complexity: O(log(n)), Space Complexity: O(1) ; Using Binary Search
# We will do a binary search to get the first occurrence of X element and then we will do a binary search to get the last occurrence of X element

def first_occurrence(l,x):
    low=0
    high=len(l)-1

    while low<=high:
        mid=(low+high)//2

        if l[mid]>x:
            high=mid-1
        elif l[mid]<x:
            low = mid+1
        else:
            if mid==0 or l[mid-1]!=l[mid]:
                return mid
            else:
                high=mid-1
    return -1

def last_occurrence(l,x):
    low=0
    high=len(l)-1

    while low<=high:
        mid=(low+high)//2

        if l[mid]>x:
            high=mid-1
        elif l[mid]<x:
            low = mid+1
        else:
            if mid==len(l)-1 or l[mid+1]!=l[mid]:
                return mid
            else:
                low=mid+1
    return -1

def k_num(l,x):
    first = first_occurrence(l,x)
    if first==-1:
        return 0
    else:
        return last_occurrence(l,x)-first+1

l=[2,4,10,10,10,18,20]
x=10
print("Number of times element occurred: ",k_num(l,x))