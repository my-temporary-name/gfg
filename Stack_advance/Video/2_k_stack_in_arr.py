# Implement K stack in an Array

class KStacks:
    def __init__(self,k,n):
        self.k = k # no. of stacks
        self.n = n # Total size of array
        self.arr = [0]*self.n
        self.top = [-1]*self.k # To store the top of each stack
        self.free = 0

        self.next = [i+1 for i in range(self.n)] # To store the next free slot in the array
        self.next[self.n-1] = -1 # -1 indicates end of free list

    def isEmpty(self,sn):
        return self.top[sn]== -1 # If top of stack is -1, then stack is empty
    
    def isFull(self):
        return self.free == -1 # If free is -1, then array is full
    
    def push(self,item,sn):
        if self.isFull():
            print("Stack Overflow")
            return
        
        insert_at = self.free
        self.free = self.next[self.free] # Update the free slot to next free slot
        self.arr[insert_at] = item # Insert the item in the array
        self.next[insert_at] = self.top[sn] # Update the next of the new item to the top of the stack
        self.top[sn] = insert_at # Update the top of the stack to the new item

    def pop(self,sn):
        if self.isEmpty(sn):
            return None

        top_of_stack = self.top[sn]
        self.top[sn] = self.next[self.top[sn]] # Update the top of the stack to the next of the top
        self.next[top_of_stack] = self.free # Update the next of the top to the free slot
        self.free = top_of_stack # Update the free slot to the top of the stack

        return self.arr[top_of_stack]
    
    def printStack(self,sn):
        top_index = self.top[sn]
        while (top_index != -1):
            print(self.arr[top_index])
            top_index = self.next[top_index]


# Driver Code
if __name__ == "__main__":
	
	kstacks = KStacks(3, 10)

	kstacks.push(15, 2)
	kstacks.push(45, 2)

	kstacks.push(17, 1)
	kstacks.push(49, 1)
	kstacks.push(39, 1)

	kstacks.push(11, 0)
	kstacks.push(9, 0)
	kstacks.push(7, 0)
    
    

	print("Popped element from stack 2 is " +
						str(kstacks.pop(2)))
	print("Popped element from stack 1 is " +
						str(kstacks.pop(1)))
	print("Popped element from stack 0 is " +
						str(kstacks.pop(0)))

	kstacks.printStack(0)
