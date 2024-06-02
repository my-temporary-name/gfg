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