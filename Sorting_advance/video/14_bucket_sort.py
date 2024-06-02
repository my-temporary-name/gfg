# Bucket sort

# 1. Consider a situation where we have numbers uniformly distributed in a range from 1 to 10**8. How can we sort them?
# 2. Consider another situation we have floating point numbers uniformly distributed in a range from 0 to 1. How can we sort them?
# Idea: hashing with chaining.

# I/P: [20,88,70,85,75,97,18,82,60] : Range: 0 to 99

# Step 1: Create an empty bucket list of size 20, i.e: 0-19, 20-39, 40-59, 60-79, 80-99. [[18], [20],[]],[70,75,60],[82,85,88,95]]
# Step 2: Sort the individual buckets. [[18], [20],[]],[60,70,75],[82,85,88,95]
# Step 3: Concatenate the buckets. [18,20,60,70,75,82,85,88,95]


# Time complexity: if k is close to n (k=n) Best case: uniform distribution: O(n).
# If all elements are in the same bucket: O(n^2). worst case.


def bucketSort(arr,k):
    rs = max(arr)+1
    bkt=[[] for i in range(k)]
    for x in arr:
        i = (k*x)//rs
        bkt[i].append(x)
    
    for i in range(k):
        bkt[i].sort()
    
    idx=0

    for i in range(k):
        for j in range(len(bkt[i])):
            arr[idx] = bkt[i][j]
            idx+=1
    
    for i in range(len(arr)):
        print(arr[i],end=" ")

arr=[30, 40, 10, 80, 5, 12, 70]
k=4
bucketSort(arr, k)