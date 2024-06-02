# Clone a Linked List with random connections

# Using Dictionary
# 1. Create an empty Dictionary d
# 2. Traverse through the list and do the following for every node:
#   d[curr]= Node(curr.data)
# 3. Traverse the original list again and do:
#   d[curr].next = d[curr.next]
#   d[curr].random = d[curr.random]
# 4. Return d[head]

from utils import Node, printList

def clone(head):
    d= dict()
    curr = head
    # Code to clone the linked list
    while curr!=None:
        d[curr] = Node(curr.data)
        curr = curr.next
    # Code connect the clone nodes
    curr = head
    while curr!= None:
        d[curr].next = d[curr.next]
        d[curr].random = d[curr.random]
        curr = curr.next
    return d[head]