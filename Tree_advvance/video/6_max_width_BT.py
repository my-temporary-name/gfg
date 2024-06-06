# Maximum width of binary tree

from collections import deque
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def getMaxWidth(root):
    if root is None:
        return 0
    
    q = deque()
    maxWidth = 0

    q.append(root)
    while q:
        count = len(q)
        maxWidth = max(count, maxWidth)

        while(count is not 0):
            count = count-1
            temp = q.popleft()
            if temp.left is not None:
                q.append(temp.left)
            
            if temp.right is not None:
                q.append(temp.right)
        
    return maxWidth

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(8)
root.right.right.left = Node(6)
root.right.right.right = Node(7)


print (getMaxWidth(root))