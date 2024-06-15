# Egg Dropping Problem
# The Egg Dropping Problem is a famous problem in dynamic programming. The problem is as follows:
# We are given n eggs and k floors. 
# We have to find the minimum number of attempts needed to find the critical floor in the worst case. 
# The critical floor is the floor from which the egg starts breaking when dropped. 
# We have to find the minimum number of attempts needed to find the critical floor in the worst case.

# Method 1: Recursion, Time Complexity: O(n*k^2)    

# Let res(f,e) be the minimum number of attempts needed to find the critical floor in the worst case with f floors and e eggs
# res = Min(max(res(x-1,e-1),res(f-x,e)))  + 1 # where 1<=x<=f
# Base Case:
# 1. res(f,1) = f # if we have only one egg, we need f attempts
# 2. res(1,e) = 1 # if we have only one floor, we need only one attempt
# 3. res(0,e) = 0 # if we have 0 floors, we need 0 attempts


import sys
def eggDrop(n,k):
    if k==1 or k==0:
        return k
    if n==1:
        return k
    min = sys.maxsize

    for x in range(1, k+1):
        res = max(eggDrop(n-1, x-1), # egg breaks
                  eggDrop(n, k-x)) # egg does not break
        
        if res<min:
            min = res
    return min+1

n = 2
k = 10
print(eggDrop(n,k)) # 4

# Method 2: Recursion + Memoization, Time Complexity: O(n*k^2)

# A Dynamic Programming based Python 
# Program for the Egg Dropping Puzzle
INT_MAX = 32767

# Function to get minimum number of trials needed in worst
# case with n eggs and k floors
def eggDrop(n, k):
	# A 2D table where entry eggFloor[i][j] will represent minimum
	# number of trials needed for i eggs and j floors.
	eggFloor = [[0 for x in range(k + 1)] for x in range(n + 1)]

	# We need one trial for one floor and0 trials for 0 floors
	for i in range(1, n + 1):
		eggFloor[i][1] = 1
		eggFloor[i][0] = 0

	# We always need j trials for one egg and j floors.
	for j in range(1, k + 1):
		eggFloor[1][j] = j

	# Fill rest of the entries in table using optimal substructure
	# property
	for i in range(2, n + 1):
		for j in range(2, k + 1):
			eggFloor[i][j] = INT_MAX
			for x in range(1, j + 1):
				res = 1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x])
				if res < eggFloor[i][j]:
					eggFloor[i][j] = res

	# eggFloor[n][k] holds the result
	return eggFloor[n][k]

# Driver program to test to printDups
n = 2
k = 10
print("Minimum number of trials in worst case with" + str(n) + "eggs and "
	+ str(k) + " floors is " + str(eggDrop(n, k)))

