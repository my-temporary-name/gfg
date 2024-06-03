# Implement 2 stacks in an array

# 1. Begin both stack from the two ends of the array
# 2. Now we can insert items in both stack as long as there is some space left in the array.

class TwoStacks:
    def __init__(self,n):
        self.size = n
        self.arr = [None]*n
        self.top1 = -1
        self.top2 = self.size

    def push1(self,x):
        if self.top1 < self.top2 - 1:
            self.top1 = self.top1+1
            self.arr[self.top1]=x
            return True
        return False
    
    def push2(self,x):
        if self.top1<self.top2-1:
            self.top2 = self.top2 - 1
            self.arr[self.top2] = x
            return True
        return False
    
    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 = self.top1 -1 
            return x
        return None
    
    def pop2(self):
        if self.top2>self.size:
            x = self.arr[self.top2]
            self.top2 = self.top2 + 1
            return x
        return None
    
    def size1(self):
        return self.top1+1
    
    def size2(self):
        return self.size - self.top2
    
# Driver code
ts = TwoStacks(5)
ts.push1(10)
ts.push2(70)
print(ts.pop1())
    
    