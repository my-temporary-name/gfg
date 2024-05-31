# count set bits: find the number of set bits (bits with value 1) in a number

# naive approach: The basic method we use to manually convert the number into binary and count the number of 1s in it.
# Time complexity: O(number of bits in the number)

def countSetBits(n):
    res =0
    while n:
        if (n%2==1):
            res+=1
        # Instead of above if condition, we can use res = res +(n&1)
        n=n//2
    return res

if __name__ =="__main__":
    print(countSetBits(5)) # 5 = 101, 2 bits are set


# Brian Kernighan’s Algorithm: The algorithm is based on the fact that the last set bit of a number n is n & (n-1).
# One by one we will unset the rightmost set bit of the number n and increment the count of set bits.
# Example n:40 = 101000, 32 = 100000, 0 = 000000 So total set bits = 2

# Time complexity: O(number of set bits)

def countSetBits(n):
    res =0
    while n:
        n= n & (n-1)
        res+=1
    return res

if __name__ =="__main__":
    print(countSetBits(40)) # 40 = 101000, 2 bits are set

# n=40: 101000
# n-1=39: 100111
# n & (n-1) = 100000

# n=32: 100000
# n-1=31: 011111
# n & (n-1) = 000000


# Lookup table method: We can create a lookup table for all 8-bit numbers and store the number of set bits in it. Works for 32-bit numbers only.

tbl =[0] * 256 # We can create a lookup table for all 8-bit numbers

def initialize():
    for i in range(256):
        tbl[i] = (i&1) + tbl[i//2]
    print(tbl[:8],tbl[8:16],tbl[16:24],tbl[24:32])

def countbits(n):
    print( n & 0xff)
    print(tbl[n & 0xff])
    
    return tbl[n & 0xff] + tbl[(n>>8) & 0xff] + tbl[(n>>16) & 0xff] + tbl[(n>>24) & 0xff]

initialize()
print(countbits(5)) # 40 = 101000, 2 bits are set