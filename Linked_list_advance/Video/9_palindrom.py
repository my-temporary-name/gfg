# Check palindrome linked list

# Naive approach:
# Use stack

def isPal(head):
    stack = []
    curr = head
    while curr!= None:
        stack.append(curr.key)
        curr=curr.next
    
    curr = head
    while curr!=None:
        if stack.pop()!=curr.key:
            return False
        curr = curr.next
    return True

# Test
from utils import Node, printList
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(1)
head.next.next.next.next = Node(1)

printList(head)
print(isPal(head))


# Effective approach: We will be using the concept of slow and fast pointer to find the middle of the linked list.
def reverseList(head):
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev


def isPal2(head):
    if head == None:
        return True
    slow,fast = head,head
    while fast.next!=None and fast.next.next!=None:
        slow = slow.next
        fast = fast.next.next
    
    rev = reverseList(slow.next)
    curr = head
    while rev!=head:
        if rev.key!=curr.key:
            return False
        rev = rev.next
        curr = curr.next
    return True

from utils import Node, printList
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(1)
head.next.next.next.next = Node(1)

printList(head)
print(isPal2(head))