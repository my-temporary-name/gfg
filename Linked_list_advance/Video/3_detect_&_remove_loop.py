# Detect and remove loop in a linked list

# 1. detect loop using Floyd's cycle detection algorithm
# 2. Move slow_p tp the beginning of the list and keep fast_p at the meeting point.
# 3. Now one by one move slow_p and fast_p one node at a time. The point at which they meet is the start of the loop.

from utils import Node, printList

def detect_Remove(head):
    slow=head
    fast=head

    # detect loop
    while fast!=None and fast.next!=None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if slow != fast:
        return
    
    # Remove loop
    slow = head
    while slow.next!=fast.next:
        slow = slow.next
        fast = fast.next
    fast.next = None

            
head = Node(10)
head.next = Node(10)
head.next.next = Node(20)


printList(head)
detect_Remove(head)
printList(head)