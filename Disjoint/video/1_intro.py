# Disjoint Set Data Structure
# Disjoint Set Data Structure is a data structure that keeps track of a set of elements partitioned into a number of disjoint (non-overlapping) subsets.
# A union-find algorithm is an algorithm that performs two useful operations on such a data structure:
# Find: Determine which subset a particular element is in. This can be used for determining if two elements are in the same subset.
# Union: Join two subsets into a single subset.

# ques: Make friends with the given pairs of people
# We are given n people and a list of pairs of people to make friends with. We have to determine the number of friends each person has.
# func: makeFriends(a,b) # it  will make friends with a and b
# func: areFriends(a, b) # it will return True if a and b are friends, otherwise False

# Naive Approach:
# Use Adjacency list or Adjacency matrix to store the friends of each person.
# Adjacency list: makeFriends() -> O(n) and areFriends() -> O(n)
# Adjacency matrix: makeFriends() -> O(n^2) and areFriends() -> O(1)

# Better Approach: Disjoint Set Data Structure, TC: O(1) for makeFriends() and areFriends()