# Segregate Even and Odd nodes in a Linked List



# Naive solution:
# 1. Find the last node reference/pointer by doing traversal.
# 2. Traverse the linked list again. For every odd node insert it after the last node and make the newly inserted node as the new last node.


# Efficient solution:
# 1. We maintain 4 variables: evenStart, evenEnd, oddStart, oddEnd
# 2. While Traversing:
# a. if current node is even, we insert it after ee and update ee to current node. Also update es if this is the first even node.
# b. if current node is odd, we insert it after oe and update oe to current node. Also update os if this is the first odd node.
# 3. Finally, we attach oddStart to evenEnd.

head = None # head of list

# Node class
class Node:
	
	def __init__(self, data):
		self.data = data # Assign data
		self.next =None

def segregateEvenOdd():

	global head
	end = head
	prev = None
	curr = head

	while (end.next != None):
		end = end.next

	new_end = end

	while (curr.data % 2 !=0 and curr != end):
		
		new_end.next = curr
		curr = curr.next
		new_end.next.next = None
		new_end = new_end.next
		
	if (curr.data % 2 == 0):
		
		head = curr

		while (curr != end):
			
			if (curr.data % 2 == 0):
				
				prev = curr
				curr = curr.next
				
			else:
				
				prev.next = curr.next

				curr.next = None

				new_end.next = curr

				new_end = curr

				curr = prev.next
			
	else:
		prev = curr

	if (new_end != end and end.data % 2 != 0):
		
		prev.next = end.next
		end.next = None
		new_end.next = end
		
def push(new_data):
	global head

	new_node = Node(new_data)

	new_node.next = head

	head = new_node

def printList():
	global head
	temp = head
	while(temp != None):
		
		print(temp.data, end = " ")
		temp = temp.next
		
	print(" ")

# Driver program to test above functions

push(11)
push(10)
push(8)
push(6)
push(5)
push(2)
push(0)
print("Original Linked List")
printList()

segregateEvenOdd()

print("Modified Linked List")
printList()
    