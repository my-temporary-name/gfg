# We have to check if given n is power of 2 or not.
# Example: 4 = yes, 5 = no

#  Naive approach: We can divide the number by 2 until it becomes 1. If at any point the number is not divisible by 2, then it is not a power of 2.

def isPowerOf2(n):
    if n==0:
        return False
    
    while n!=1:
        if n%2!=0:
            return False
        n=n//2
    return True

if __name__ =='__main__':   
    print(isPowerOf2(4)) # True
    print(isPowerOf2(5)) # False
    print(isPowerOf2(0)) # False


# Method 3: Using brain Kernighan’s Algorithm

def isPowerOf2(n):
    if n==0:
        return False
    return (n & (n-1) == 0) 

if __name__ =='__main__':   
    print( "Second method")
    print(isPowerOf2(4)) # True
    print(isPowerOf2(5)) # False
    print(isPowerOf2(0)) # False