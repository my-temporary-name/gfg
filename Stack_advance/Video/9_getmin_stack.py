# Design a stack that supports getMin()
# Design a function that returns the minimum element from the stack in O(1) time complexity.

# Idea:
# Maintain two stacks: one to store the elements and the other to store the minimum element.
# as = auxiliary stack to store the minimum element, ms = main stack to store the elements

# push(x):
# ms.push(x)
# if (as.top()>=ms.top()):
#    as.push(x)

# pop()
# if (ms.top() == as.top()):
#   as.pop()
# ms.pop()

# Class to make a Node

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

	def __str__(self):
		return "Node({})".format(self.value)

	__repr__ = __str__


class Stack:
	def __init__(self):
		self.top = None
		self.count = 0
		self.minimum = None

	def __str__(self):
		temp = self.top
		out = []
		while temp:
			out.append(str(temp.value))
			temp = temp.next
		out = '\n'.join(out)
		return ('Top {} \n\nStack :\n{}'.format(self.top, out))

	__repr__ = __str__

	def getMin(self):
		if self.top is None:
			return "Stack is empty"
		else:
			print("Minimum Element in the stack is: {}" .format(self.minimum))


	def isEmpty(self):
		if self.top == None:
			return True
		else:
			return False

	def __len__(self):
		self.count = 0
		tempNode = self.top
		while tempNode:
			tempNode = tempNode.next
			self.count += 1
		return self.count

	def peek(self):
		if self.top is None:
			print("Stack is empty")
		else:
			if self.top.value < self.minimum:
				print("Top Most Element is: {}" .format(self.minimum))
			else:
				print("Top Most Element is: {}" .format(self.top.value))


	def push(self, value):
		if self.top is None:
			self.top = Node(value)
			self.minimum = value

		elif value < self.minimum:
			temp = (2 * value) - self.minimum
			new_node = Node(temp)
			new_node.next = self.top
			self.top = new_node
			self.minimum = value
		else:
			new_node = Node(value)
			new_node.next = self.top
			self.top = new_node
		print("Number Inserted: {}" .format(value))

	def pop(self):
		if self.top is None:
			print("Stack is empty")
		else:
			removedNode = self.top.value
			self.top = self.top.next
			if removedNode < self.minimum:
				print("Top Most Element Removed :{} " .format(self.minimum))
				self.minimum = ((2 * self.minimum) - removedNode)
			else:
				print("Top Most Element Removed : {}" .format(removedNode))


# Driver program to test above class
if __name__ == '__main__':

    stack = Stack()

    # Function calls
    stack.push(3)
    stack.push(5)
    stack.getMin()
    stack.push(2)
    stack.push(1)
    stack.getMin()
    stack.pop()
    stack.getMin()
    stack.pop()
    stack.peek()
	
# Next video shows the improved version of this code. which only uses one stack instead of two.