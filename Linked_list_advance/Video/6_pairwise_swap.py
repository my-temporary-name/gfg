# Pairwise swap nodes of a linked list

# example: 1->2->3->4->5->6->7->8->NULL
# output: 2->1->4->3->6->5->8->7->NULL

# Naive approach:
# #Run a loop while we have at least one node ahead
# a. Swap data of current node with its next node.
# b. Move current by 2 positions.

def pairSwap(head):
    curr = head
    while curr!=None and curr.next!=None:
        curr.key, curr.next.key = curr.next.key, curr.key
        curr = curr.next.next
    return head

# Test
from utils import Node, printList
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

printList(head)
head = pairSwap(head)
printList(head)

# Effective approach:

def pairwiseSwap(head):
    if head == None or head.next == None:
        return head
    
    curr = head.next.next
    prev = head
    head = head.next
    head.next = prev

    while curr!=None and curr.next!=None:
        prev.next = curr.next
        prev = curr
        next = curr.next.next
        curr.next.next = curr
        curr = next
    prev.next = curr
    return head

from utils import Node, printList
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

printList(head)
head = pairwiseSwap(head)
printList(head)