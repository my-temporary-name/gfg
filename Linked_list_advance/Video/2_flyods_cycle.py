# Detect loop in linked list using Floyd's cycle detection algorithm

# 1. Initialize slow and fast pointers to head.
# 2. Move slow pointer by one and fast pointer by two. and check if they meet at some point.

from utils import Node
from utils import printList

def isLoop(head):
    slow_p = head
    fast_p = head
    while fast_p != None and fast_p.next!=None and slow_p!=None:
        slow_p=slow_p.next
        fast_p=fast_p.next.next
        if slow_p==fast_p:
            return True
    return False

# Test
# inserting new values
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
 
# adding a loop for the sake
# of this example
temp = head
while (temp.next != None):
    temp = temp.next
 
temp.next = head

if (isLoop(head)):
    print("Loop exists in the Linked List")
else:
    print("Loop does not exists in the Linked List")

