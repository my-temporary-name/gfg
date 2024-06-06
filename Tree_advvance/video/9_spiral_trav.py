# Tree Traversal in Spiral Form

class newNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printSpiral(root): # Function to print the spiral traversal of tree
    h = height(root)
    """ltr Left to Right. If this variable
	is set, then the given level is traversed
	from left to right. """

    ltr = False
    for i in range(1, h+1):
        printGivenLevel(root, i, ltr)
        """Revert ltr to traverse next level in opposite direction"""
        ltr = not ltr

# Print nodes at a given level

def printGivenLevel(root, level, ltr):
    if(root==None):
        return
    if(level==1):
        print(root.data, end=" ")
    elif(level>1):
        if (ltr):
            printGivenLevel(root.left, level-1, ltr)
            printGivenLevel(root.right, level-1, ltr)
        else:
            printGivenLevel(root.right, level-1, ltr)
            printGivenLevel(root.left, level-1, ltr)
    

""" Compute the "height" of a tree -- the number of
	nodes along the longest path from the root node
	down to the farthest leaf node."""

def height(node):
    if node==None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        # use larger one
        if lheight>rheight:
            return lheight+1
        else:
            return  rheight+1
        



if __name__ == '__main__':
	root = newNode(1)
	root.left = newNode(2)
	root.right = newNode(3)
	root.left.left = newNode(7)
	root.left.right = newNode(6)
	root.right.left = newNode(5)
	root.right.right = newNode(4)
	print("Spiral Order traversal of binary tree is")
	printSpiral(root)