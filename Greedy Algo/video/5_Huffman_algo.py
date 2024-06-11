# Huffman Coding Algorithm
# In computer science and information theory, Huffman coding is an optimal prefix code used for lossless data compression. 
# The term refers to the use of a variable-length code table for encoding a source symbol (such as a character in a file) 
# where the variable-length code table has been derived in a particular way based on the estimated probability of occurrence for each possible value of the source symbol. 
# It was first introduced by David A. Huffman in 1952.

# used for lossless data compression
# Variable length coding



import heapq

class node:
    def __init__(self, freq, symbol, left = None, right = None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''
    
    def __lt__(self,nxt): # this is required for min heap
        return self.freq < nxt.freq # return the node with minimum frequency

def printNodes(node, val=''):
	
	newVal = val + str(node.huff)

	if(node.left):
		printNodes(node.left, newVal)
	if(node.right):
		printNodes(node.right, newVal)
	if(not node.left and not node.right):
		print(f"{node.symbol} -> {newVal}")

chars = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [ 5, 9, 12, 13, 16, 45]
nodes = []

for x in range(len(chars)):
    heapq.heappush(nodes, node(freq[x], chars[x]))

while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)

    left.huff = '0'
    right.huff = '1'

    newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
    heapq.heappush(nodes, newNode)

printNodes(nodes[0])