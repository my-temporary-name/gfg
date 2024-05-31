# Tower of Hanoi
# With the help of middle rod, move all the disks from source rod to destination rod such that no disk is placed on top of smaller disk.

# Roughly, the steps are:
# TOH (n,A,B, C) # A: Source rod, B: Helper rod, C: Destination rod
# -> TOH(n-1, A, C, B) # Move from A to B using C
# -> Move Disc from A to C
# -> TOG(n-1, B, A, C) # Move from B to C using A

def toh(n, A,B, C): # Time complexity: O(2^n) ; Space complexity: O(n)
    if n==1:
        print("Move 1 from ",A, "to ", C)
    else:
        toh(n-1,A,C,B)
        print("Move ",n,"from ",A,"to ",C)
        toh(n-1,B,A,C)

n = 3
toh(n, "A", "B", "C")