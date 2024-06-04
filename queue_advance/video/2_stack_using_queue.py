# Implement stack using queue

from collections import deque

class stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    
    def push(self, x ):
        self.q2.append(x)

        while self.q1:
            self.q2.append(self.q1.popleft())
        
        self.q1, self.q2 = self.q2, self.q1
    
    def pop(self):
        if self.q1:
            self.q1.popleft()
        
    def top(self):
        if self.q1:
            return self.q1[0]
        else:
            return None
        
    def size(self):
        return len(self.q1)
    
s = stack()
s.push(3)
s.push(4)
s.push(5)
s.push(6)
print(s.size())
print(s.top())
s.pop()
print(s.top())