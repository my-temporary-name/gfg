# Count Nodes of Complete Binary Tree
# Binary tree is complete binary tree if all levels are completely filled except possibly the last level and the last level has all keys as left as possible

# Idea is to find the height of left and right subtree and if they are equal then the tree is complete binary tree and we can return 2^h-1

class node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def left_height(node):
    ht=0
    while(node):
        ht+=1
        node = node.left
    return ht

def right_height(node):
    ht =0
    while(node):
        ht+=1
        node = node.right
    return ht

def TotalNodes(root):
    if(root == None):
        return 0
    
    lh = left_height(root)
    rh = right_height(root)

    if lh==rh:
        return (1<<lh)-1
    return 1+ TotalNodes(root.left) + TotalNodes(root.right)

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(9)
root.right.right = node(8)
root.left.left.left = node(6)
root.left.left.right = node(7)

print(TotalNodes(root))