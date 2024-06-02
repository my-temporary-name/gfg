# Reverse a Linked list in group of given size k

# I/P: 1->2->3->4->5->6->7->8->NULL and k = 3
# O/P: 3->2->1->6->5->4->8->7->NULL

class Node:
    def __init__(self, k):
        self.key = k
        self.next = None

def printList(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next
    print()

def iteRevK(head,k):
    curr = head
    prev_first = head
    first_pass = True
    while curr!= None :
        first, prev = None, None
        count = 0 
        while curr!= None and count<k :
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count+=1
        if(first_pass):
            head = prev
            first_pass = False
        else:
            prev_first.next = prev
            prev_first=first
    return head
    
        

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head.next.next.next.next.next = Node(60)

printList(head)

head = iteRevK(head,3)

printList(head)

# Time complexity: O(n) , Space complexity: O(1)