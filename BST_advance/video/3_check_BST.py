# check BST or Not

# for every node
# 1. Find maximum value in left subtree
# 2. Find minimum value in right subtree
# check that the value of current node is greater than maximum value of left subtree and less than minimum value of right subtree

INT_MAx = 4294967296
INT_MIN = -4294967296
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isBST(node):
    return isBSTUtil(node, INT_MIN, INT_MAx)

def isBSTUtil(node, mini, maxi):
    if node is None:
        return True
    
    if node.data < mini or node.data > maxi:
        return False
    
    return isBSTUtil(node.left, mini, node.data-1) and isBSTUtil(node.right, node.data+1, maxi)

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

if (isBST(root)):
	print("Is BST")
else:
	print("Not a BST")



# Please recheck this code
# # Efficient Approach: TC= O(n), SC= O(n)
maxValue = 4294967296
minValue = -4294967296

class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None

def isBST2(node,mini,maxi):
    if node == None:
        return 1
    #  if (node.left !=None and maxValue(node.left) >= node.data):
    #       return 0
    #  if (node.left !=None and minValue(node.right) <= node.data):
    #       return 0
     
    #  if (~isBST2(node.left) or ~isBST2(node.right)):
    #       return 0
     
    #  return 1
    return (root.key>mini and root.key<maxi and isBST2(root.left, mini, root.key) and isBST(root.right, root.key, maxi))

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

if (isBST2(root,INT_MAx,INT_MIN)):
	print("Is BST")
else:
	print("Not a BST")