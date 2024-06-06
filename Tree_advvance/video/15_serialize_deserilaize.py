# Serialize and Deserialize Binary Tree
# Converting a Tree to a string is known as serialization and converting a string to tree is known as deserialization.

# Use -1 for Null. Assumption: -1 is not a present in the tree as data.
#   10
#  /  \
# 20  30
# Serialize: 10 20 -1 -1 30 -1 -1 (preorder traversal)

#    10
#   /  
#  20
# Serialize: 10 20 -1 -1 -1 (preorder traversal)

# In deserialization: 10 20 -1 -1 30 -1 -1 
# 10 is root, 20 is left child of 10 and 30 is right child of 10
#         10
#        /  \
#       20  30
#     /  \  /  \
#  Null Null Null Null

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def serialize(Self,root):
        if not root:
            return None
        
        stack = [root]
        l=[]

        while stack:
            t= stack.pop()
            if not t:
                l.append("#")
            else:
                l.append(str(t.val))
                stack.append(t.right)
                stack.append(t.left)
        return ",".join(l)

    def deserialize(self, data):
        if not data:
            return None
        global t
        t=0
        arr = data.split(",")
        return self.helper(arr)
    
    def helper(self,arr):
        global t
        if arr[t]=="#":
            return None
        
        root = Node(int(arr[t]))
        t+=1
        root.left = self.helper(arr)
        t+=1
        root.right = self.helper(arr)
        return root
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.val, end = " ")
            self.inorder(root.right)

if __name__ == '__main__':
    # Construct a tree shown in the above figure
    tree = BinaryTree()
    tree.root = Node(20)
    tree.root.left = Node(8)
    tree.root.right = Node(22)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(12)
    tree.root.left.right.left = Node(10)
    tree.root.left.right.right = Node(14)
 
    serialized = tree.serialize(tree.root)
    print("Serialized view of the tree:")
    print(serialized)
    print()
 
    # Deserialize the stored tree into root1
    t = tree.deserialize(serialized)
 
    print("Inorder Traversal of the tree constructed from serialized String:")
    tree.inorder(t)