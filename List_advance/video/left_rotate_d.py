# Left Rotate by d places
# Example: [10,20,30,40,50], d=2 --> [30,40,50,10,20]

# Method 1: Using list slicing
l = [10,20,30,40,50]
d= 2
print(l[d:]+l[:d])

# Method 2: Using deque

from collections import deque

l = [10,20,30,40,50]
d=2
dq= deque(l)
dq.rotate(-d) # Deque has a rotate method that can be used to rotate the elements of the deque by a specified number of steps.
l  =list(dq)
print("Using deque:",l)

# Method 3: Using for loop ; Time complexity: O(n*d) : d is there because we are rotating d times after each pop, Space complexity: O(d) bcz we have to save the popped elements in a list
l = [10,20,30,40,50]
d=2

for i in range(d):
    l.append(l.pop(0))

print("Using for loop:",l)

# Method 4: By reversing the list
# Example: [10,20,30,40,50], d=2
# Step 1: Reverse the first d elements: [20,10,30,40,50]
# Step 2: Reverse the remaining elements: [20,10,50,40,30]
# Step 3: Reverse the whole list: [30,40,50,10,20]
# Time complexity: O(n), Space complexity: O(1)

def reverse(l,b,e):
    while b<e:
        l[b], l[e] = l[e],l[b]
        b+=1
        e-=1

l = [10,20,30,40,50]
d=2
n = len(l)

reverse(l,0,d-1)
print("\n\nAfter reversing first d elements:",l)
reverse(l,d,n-1)
print("After reversing remaining elements:",l)
reverse(l,0,n-1)


print("Using reverse:",l)

# If d =0 , return the same list
# If d > n. return the list after rotating d%n times