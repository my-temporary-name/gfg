# Iterative Preorder Traversal:


class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None

def itrPreorder(root):
    if root is None:
        return
    
    st = [root]

    while len(st)>0:
        curr = st.pop()
        print(curr.key)

        if curr.right is not None:
            st.append(curr.right)
        
        if curr.left is not None:
            st.append(curr.left)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(60)

itrPreorder(root)


# Space optimized soltuion
class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

def preorderIter(root):
    if root == None:
        return
    
    st = []

    curr = root

    while len(st) or curr!=None:
        while curr!=None:
            print(curr.data, end=" ")
            if curr.right!=None:
                st.append(curr.right)
            curr = curr.left

        if len(st)>0:
            curr = st[-1]
            st.pop()

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.left.left = Node(70)
root.left.right = Node(50)
root.right.left = Node(60)
root.left.left.right = Node(80)

preorderIter(root)