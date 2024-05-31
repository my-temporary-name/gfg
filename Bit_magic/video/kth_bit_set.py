# check the Kth bit is set or not
# Example: 5 = 101, k=1, then 1st bit is set
# Problem Statement: Given an integer number and an index, we will have to determine whether the ith bit of the number is set (equal to 1) or not (equal to 0).

# Method 1: Using left shift operator

def isKthBitSet(n,k):
    if n & (1<<(k -1)):
        print("SET")
    else:
        print("Not set")

if __name__ =='__main__':
    n=5
    k=3
    isKthBitSet(n,k)

# n=5 : 000...0101
# k=3
# 1<<k-1 = 1<<2 = 000...0100
# n & (1<<k-1) = 000...0101 & 000...0100 = 000...0100 that is not equal to 0 so 3rd bit is set

# Method 2: Using right shift operator

def isKthBitSet(n,k):
    if 1 & (n>>(k-1)):
        print("SET")
    else:
        print("Not set")

if __name__ =='__main__':
    n=5
    k=3
    isKthBitSet(n,k)
