# convert a binary tree to doubly linked list

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.data = val

prev = None

def BinaryTree2DLL(root):
    if root is None:
        return root
    
    head = BinaryTree2DLL(root.left)

    global prev

    if prev is None:
        head = root

    else:
        root.left = prev
        prev.right = root
    
    prev = root

    BinaryTree2DLL(root.right)
    return head

def printDLL(head):
    while head is not None:
        print(head.data, end = " ")
        head = head.right

root = Node(10)
root.left = Node(12)
root.right = Node(15)
root.left.left = Node(25)
root.left.right = Node(30)
root.right.left = Node(36)

head = BinaryTree2DLL(root)

printDLL(head)