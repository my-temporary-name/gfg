# Burn Binary tree from leaf
# This means that we have to burn the leaf node and then the parent node and so on and return the time taken to burn the whole tree.

# Idea is to find farthest node from the given leaf.
# Python program to find minimum time required
# to burn the binary tree completely

# Definition for a binary tree node


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


'''
	***********ADDITIONAL INFO*************
	lDepth - maximum height of left subtree
	rDepth - maximum height of right subtree
	contains - stores true if tree rooted at current node
			contains the first burnt node
	time - time to reach fire from the initially burnt leaf
		node to this node
'''


class Info:
	def __init__(self):
		self.lDepth = 0
		self.rDepth = 0
		self.contains = False
		self.time = -1


class Solution:
	# Class Variable
	res = 0

	'''
		Function to calculate time required to burn
		tree completely

		node - address of current node
		info - extra information about current node
		target - node that is fired
		res - stores the result
	'''

	def calcTime(self, node, info, target):
		# Base case: if root is null
		if node == None:
			return info

		if node.left == None and node.right == None:
			# If current node is the first burnt node
			if node.val == target:
				info.contains = True
				info.time = 0
			return info

		# Information about left child of root
		leftInfo = Info()
		leftInfo = self.calcTime(node.left, leftInfo, target)

		# Information about right child of root
		rightInfo = Info()
		rightInfo = self.calcTime(node.right, rightInfo, target)

		# If left subtree contains the fired node then
		# time required to reach fire to current node
		# will be (1 + time required for left child)
		info.time = leftInfo.time + \
			1 if (node.left and leftInfo.contains) else -1

		# If right subtree contains the fired node then
		# time required to reach fire to current node
		# will be (1 + time required for right child)
		if info.time == -1:
			info.time = rightInfo.time + \
				1 if (node.right and rightInfo.contains) else -1

		# Storing(true or false) if the tree rooted at
		# current node contains the fired node
		info.contains = (node.left and leftInfo.contains) or (
			node.right and rightInfo.contains)

		# Calculate the maximum depth of left subtree
		info.lDepth = 0 if (not node.left) else (
			1+max(leftInfo.lDepth, leftInfo.rDepth))

		# Calculate the maximum depth of right subtree
		info.rDepth = 0 if (not node.right) else (
			1+max(rightInfo.lDepth, rightInfo.rDepth))

		# Calculating answer
		if info.contains:
			# If left subtree exists and
			# it contains the fired node
			if node.left and leftInfo.contains:
				# calculate result
				self.res = max(self.res, info.time+info.rDepth)

			# If right subtree exists and it
			# contains the fired node
			if node.right and rightInfo.contains:
				# calculate result
				self.res = max(self.res, info.time+info.lDepth)

		return info

	# Driver function to calculate minimum
	# time required
	def solve(self, root, target):
		info = Info()
		self.calcTime(root, info, target)
		return self.res


# Driver Code
if __name__ == '__main__':
	# Construct tree shown in the above example
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.left.left = TreeNode(4)
	root.left.right = TreeNode(5)
	root.right.left = TreeNode(6)
	root.left.left.left = TreeNode(8)
	root.left.right.left = TreeNode(9)
	root.left.right.right = TreeNode(10)
	root.left.right.left.left = TreeNode(11)

	# Target Leaf Node
	target = 11

	# Print min time to burn the complete tree
	s = Solution()
	print(s.solve(root, target))

