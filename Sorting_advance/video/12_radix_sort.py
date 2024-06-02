# Radix Sort

# counting sort is a linear time sorting algorithm that sort in O(n+k) time when elements are in range from 1 to k
# radix sort:

# 319, 212, 6, 8, 100, 50
# 1. Re-write number with leading zeros: 319, 212, 006, 008, 100, 050
# 2. Stable sort according to last digit (Least significant digit): 100, 050, 212, 006, 008, 319
# 3. Stable sort according to second last digit: 100, 006, 008, 212, 319, 050
# 4. Stable sort according to most significant digit: 006, 008, 050, 100, 212, 319

def countingSort(arr, exp):
    output =[0]*len(arr)
    count = [0]*10
    for i in range(0, len(arr)):
        index = (arr[i]//exp)%10
        count[index]+=1
    for i in range(1,10):
        count[i]+=count[i-1]
    
    i = len(arr)-1
    while i>=0:
        index = (arr[i]//exp)%10
        output[count[index]-1] = arr[i]
        count[index]-=1
        i-=1
    for i in range(0,len(arr)):
        arr[i]=output[i]



def radixSort(arr):
    mx=max(arr)
    exp=1
    while(mx/exp)>0:
        countingSort(arr, exp)
        exp*=10

arr = [319,212,6,8,100,50]
A = radixSort(arr)
            
for i in range(len(arr)):
    print(arr[i],end=" ")


# Time Complexity: O(d *(n+b)) d is number of digits in the input number, n is number of elements, b is base of numbers
# Space Complexity: O(n+b)