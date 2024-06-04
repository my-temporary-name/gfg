# Reverse a queue using recursion

# Use stack to reverse a queue; TC: O(n) ; SC: O(n)

from collections import deque

def reverse_queue(q):
    st = []
    while q:
        st.append(q.popleft())
    while st:
        q.append(st.pop())

q = deque()
q.append(1)
q.append(2)
q.append(3)

reverse_queue(q)

print(q)

# recursive function to reverse a queue ; TC: O(n) ; SC: O(n)

def revQ(q):
    if(len(q)==0):
        return
    
    x = q.popleft()
    revQ(q)
    q.append(x)

q = deque()
q.append(1)
q.append(2)
q.append(3)

revQ(q)

print(q)