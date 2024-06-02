# Merge two sorted linked lists without using any extra space

def sortedMerge(a,b):
    if a==None:
        return b
    if b==None:
        return a
    head,tail= None,None
    if a.key<=b.key:
        head=tail=a
        a=a.next
    else:
        head=tail=b
        b=b.next
    while a!=None and b!=None:
        if a.key<=b.key:
            tail.next = a 
            tail = a
            a = a.next
        else:
            tail.next = b
            tail = b
            b= b.next
    if a==None:
        tail.next = b
    else:
        tail.next=a
    return head

# Test
from utils import Node, printList
a = Node(5)
a.next = Node(10)
a.next.next = Node(15)
a.next.next.next = Node(40)

b = Node(2)
b.next = Node(3)
b.next.next = Node(20)
b.next.next.next = Node(25)

printList(a)
printList(b)
head = sortedMerge(a,b)
printList(head)