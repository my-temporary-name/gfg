# Construct binary tree from Inorder and Preorder traversals

class Node:
    def __init__(self,x):
        self.left = None
        self.right = None
        self.data = x

def builtTree(inn, pre, inStrt, inEnd):
    global preIndex, mp

    if inStrt > inEnd:
        return None
    
    curr = pre[preIndex]
    preIndex +=1

    tNode = Node(curr)

    if inStrt == inEnd:
         return tNode
    inIndex = mp[curr]
    tNode.left = builtTree(inn, pre, inStrt, inIndex-1)
    tNode.right = builtTree(inn, pre, inIndex+1, inEnd)
    return tNode


def buldTreeWrap(inn, pre, lenn):
    global mp
    for i in range(lenn):
         mp[inn[i]] = i
    return builtTree(inn, pre, 0, lenn-1)


def printInorder(node):
    if node == None:
         return 
    
    printInorder(node.left)
    print(node.data, end = " ")
    printInorder(node.right)
     


if __name__ == '__main__':
	
	mp = {}
	preIndex = 0

	inn = [ 'D', 'B', 'E', 'A', 'F', 'C' ]
	pre = [ 'A', 'B', 'D', 'E', 'C', 'F' ]
	lenn = len(inn)

	root = buldTreeWrap(inn, pre,lenn)

	printInorder(root)