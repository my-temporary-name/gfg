# Delete operation in a Trie

# Idea:
# 1. We write a Recursive Function.
# 2. We first traverse to the last node, we mark it not end of the word.
# 3. If this node is empty, we delete this node.
# 4. If parent of this node had only one child and not end of word, we remove parent node as well.]
# 5. We repeat the above step for parent of parent node and so on.
