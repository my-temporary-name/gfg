# Intersection point of Two Linked Lists

from utils import Node, printList
#  first method: TC = (n+m) SC = O(m)

def getIntersect(head1, head2):
    s= set()
    curr = head1
    while curr!= None:
        s.add(curr)
        curr = curr.next
    
    curr = head2
    while curr!= None:
        if curr in s:
            return curr.key
        curr = curr.next
    return -1

head = Node(10)
head.next = Node(10)
head.next.next = Node(20)

ahead = Node(10)
ahead.next = Node(10)
ahead.next.next = Node(20)


printList(head)
#should not do anything as these are different lists
print(getIntersect(head,ahead))
printList(head)


# Second method: TC = O(n+m) SC = O(1)

def getSize(head):
    if head is None:
        return 0
    count=0
    while head != None:
        count+=1
        head=head.next
    return count

def get_intersect2(d,head1,head2):
    curr1= head1
    curr2 = head2

    for  i in range(d):
        if curr1 == None:
            return -1
        curr1 = curr1.next
    while curr1!=None and curr2!=None:
        if curr1 == curr2:
            return curr1.key
        curr1 = curr1.next
        curr2 = curr2.next

head = Node(10)
head.next = Node(10)

ahead = Node(10)
ahead.next = Node(10)
ahead.next.next = Node(20)


printList(head)
#should not do anything as these are different lists
d = abs(getSize(head)- getSize(ahead))
print(get_intersect2(d,head,ahead))