# find kth smallest element in BST


# Naive Approach:
# Do simple inorder traversal and store the elements in a list: TC = O(n), SC = O(n)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def printkth(root,k):
    if root!=None:
        printkth(root.left,k)
        printkth.count+=1

        if printkth.count == k:
            print(root.key)
            return
        printkth(root.right, k )

root = Node(15)
root.left = Node(5)
root.left.left = Node(3)
root.right = Node(20)
root.right.left = Node(18)
root.right.left.left = Node(16)
root.right.right = Node(80)

k = 3 
printkth.count = 0 

print("kth smallest:", end = " ")
printkth(root, k)


# efficient approach: TC = O(h+k), SC = O(h)
# Idea is to while doing inorder traversal, keep track of the count of nodes visited so far
# if count == k, then print the node and return

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def insert(root, x ):
    if root == None:
        return Node(x)
    if x<root.data:
        root.left = insert(root.left,x)
    elif x>root.data:
        root.right = insert(root.right,x)
    return root

def KthSmallest(root):
    global k
    if root == None:
        return None
    left = KthSmallest(root.left)

    if left!=None:
        return left
    
    k-=1
    if k==0:
        return root
    return KthSmallest(root)


def printKthSmallest(root):

	res = KthSmallest(root)

	if (res == None):
		print("There are less than k nodes in the BST")
	else:
		print("K-th Smallest Element is ", res.data)


if __name__ == '__main__':

	root = None
	keys = [20, 8, 22, 4, 12, 10, 14]

	for x in keys:
		root = insert(root, x)

	k = 3

	printKthSmallest(root)
