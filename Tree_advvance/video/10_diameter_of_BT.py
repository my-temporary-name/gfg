# Diameter of Binary Tree
# The diameter of a tree is the number of nodes on the longest path between two leaves in the tree. The path may or may not pass through the root.

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    return 1+max(height(node.left), height(node.right))

def diameter(root): # time complexity: O(n^2)
    if root is None:
        return 0
    lheight = height(root.left)
    rheight = height(root.right)

    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)

    return max(lheight + rheight + 1, max(ldiameter, rdiameter))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(diameter(root))


# Efficient solution: Time Complexity: O(n)
# 1. precompute height of all node by calling recursive height function
# 2. store these height in a dictionary with node as key and height as value
# 3. The recursive diameter function simply returns the height of the node if it is already computed

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Height:
    def __init__(self):
        self.h = 0

def diameterOpt(root, height):
    lh = Height()
    rh = Height()

    if root is None:
        height.h=0
        return 0
    
    ldiameter = diameterOpt(root.left, lh)
    rdiameter = diameterOpt(root.right, rh)

    height.h = max(lh.h, rh.h) + 1
    return max(lh.h + rh.h + 1, max(ldiameter, rdiameter))

def diameter(root):
    height = Height()
    return diameterOpt(root, height)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print(diameter(root))