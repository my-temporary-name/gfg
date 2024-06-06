# Pair sum with given BST
# Find a pair with given sum in a BST


class Node:
    def __init__(self, k):
        self.key = k 
        self.left = None
        self.right = None

def ispairsum(root, sum, s):
    if root == None:
        return False
    if ispairsum(root.left, sum, s):
        return True
    if sum - root.key in s:
        print("Pair Found: {} + {} = {}".format(sum - root.key,root.key, sum))
        return True
    else:
        s.add(root.key)
    
    return ispairsum(root.right, sum, s)


root = Node(10)
root.left = Node(8)
root.right = Node(20)
root.left.left = Node(4)
root.left.right = Node(9)
root.right.left = Node(11)
root.right.right = Node(30)
root.right.right.left = Node(25)

sum = 33 
s = set()
if not ispairsum(root,sum, s) :
    print("No such value are found")