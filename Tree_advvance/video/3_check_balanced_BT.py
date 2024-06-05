# check balanced binary tree
# Binary tree is balanced if the height of the two subtrees of any node never differ by more than one.

# Naive solution:
# For each node, we recursively calculate the height of the left and right subtrees. 
# If the difference between the heights is greater than one, we return False. Otherwise, we return True.

class Node:
    def __init__(self,k):
        self.left = None
        self.right = None
        self.key = k

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def isBalanced(root):

    if root is None:
        return True
    
    lh = height(root.left)
    rh = height(root.right)

    if (abs(lh-rh)<=1) and isBalanced(root.left) is True and isBalanced(root.right) is True:
        return True
    
    return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)
if isBalanced(root):
	print("Tree is balanced")
else:
	print("Tree is not balanced")
     

# Optimized solution: Time Complexity: O(n)
# Idea is to return -1 if the tree is not balanced and return the height of the tree if it is balanced.
# We recursively calculate the height of the left and right subtrees. If the difference between the heights is greater than one, we return -1. Otherwise, we return the height of the tree.

def isBalanced2(root):
     if root is None:
          return True
     lh = isBalanced2(root.left)

     if lh==-1:
          return -1
     
     rh = isBalanced2(root.right)
     if rh == -1:
          return -1
     
     if (abs(lh-rh) > 1):
          return -1
     
     else:
          return max(lh,rh) + 1
     
if __name__ == '__main__':
	root = Node(10)
	root.left = Node(5)
	root.right = Node(30)
	root.right.left = Node(15)
	root.right.right = Node(20)
	if (isBalanced2(root) == -1):
		print("Not Balanced")
	else:
		print("Balanced")