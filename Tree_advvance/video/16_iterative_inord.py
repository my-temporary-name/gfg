# Iterative Inorder Traversal:

# Idea is to use stack to store the nodes and traverse the tree in inorder fashion. TC = O(n) and SC = O(n)

class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None

def itrInorder(root):
    if root is None:
        return
    
    st = []
    curr = root
    while curr is not None:
        st.append(curr)
        curr = curr.left

    while len(st) > 0:
        curr = st.pop()
        print(curr.key)
        curr = curr.right

        while curr is not None:
            st.append(curr)
            curr = curr.left

# Driver Code

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)

itrInorder(root)