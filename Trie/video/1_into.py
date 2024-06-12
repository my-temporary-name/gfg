# Trie Data Structure
# Trie is an efficient information reTrieval data structure. 
# Using Trie, search complexities can be brought to optimal limit (key length). 
# If we store keys in binary search tree, a well balanced BST will need time proportional to M * log N, where M is maximum string length and N is number of keys in tree. 
# Using Trie, we can search the key in O(M) time. However the penalty is on Trie storage requirements.

# Trie is Efficient for:
# Searching strings with common prefix, insertion and deletion of strings, lexicographically sorting of strings, prefix matching

# Trie Representation

class TrieNode: # Trie Node class
	
	def __init__(self):
		self.children = [None]*26

		self.isEndOfWord = False

class Trie: # Trie data structure class
	
	def __init__(self): 
		self.root = self.getNode()

	def getNode(self): # Returns new trie node (initialized to NULLs)
	
		return TrieNode()

	def _charToIndex(self,ch): # private helper function that converts key current character into index
		
		return ord(ch)-ord('a')


	def insert(self,key): # If not present, inserts key into trie. If the key is prefix of trie node, just marks leaf node
		
		pCrawl = self.root
		length = len(key)
		for level in range(length):
			index = self._charToIndex(key[level])

			if not pCrawl.children[index]:
				pCrawl.children[index] = self.getNode()
			pCrawl = pCrawl.children[index]

		pCrawl.isEndOfWord = True

	def search(self, key): # Returns true if key presents in trie, else false
		
		pCrawl = self.root
		length = len(key)
		for level in range(length):
			index = self._charToIndex(key[level])
			if not pCrawl.children[index]:
				return False
			pCrawl = pCrawl.children[index]

		return pCrawl.isEndOfWord

def main():

	keys = ["the","a","there","anaswe","any",
			"by","their"]
	output = ["Not present in trie",
			"Present in trie"]

	t = Trie()

	for key in keys:
		t.insert(key)

	print("{} ---- {}".format("the",output[t.search("the")]))
	print("{} ---- {}".format("these",output[t.search("these")]))
	print("{} ---- {}".format("their",output[t.search("their")]))
	print("{} ---- {}".format("thaw",output[t.search("thaw")]))

if __name__ == '__main__':
	main()
