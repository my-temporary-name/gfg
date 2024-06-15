# Optimal Strategy for a Game
# 
# Rules:
# a. Two player game
# b. Players take turns one by one
# c. Given no. of coins is even initially
# d. You always make the first move
# e. Both Players play optimally

# You need to find the maximum no. of value you can collect.
# you have to pick from one of the ends of the array. and opponent will also pick from one of the ends of the array or next element from your pick.
# eg: arr: [2,3,15,7]
# o/p 17. You will pick 2 then opponent will pick 3 then you will pick 15 then opponent will pick 7
# Even if you pick 2 and opponent pick 7 then you will pick 15 and opponent will pick 3. So, you will get 17.

# Method 1: Recursion
# 1. we find the sum of values before recursion call
# 2. We make two recursive call and take the maximum of the two
#   a. Pick  the left corner coin
#  b. Pick the right corner coin

# Method 1: Recursion, TC: O(2^n)

def oSRec(arr, i, j, Sum):

	if (j == i + 1):
		return max(arr[i], arr[j])

	return max((Sum - oSRec(arr, i + 1, j, Sum - arr[i])),
			(Sum - oSRec(arr, i, j - 1, Sum - arr[j])))




def optimalStrategyOfGame(arr, n):

	Sum = 0
	Sum = sum(arr)
	return oSRec(arr, 0, n - 1, Sum)

arr = [2,3,15,7]
n = len(arr)
print(optimalStrategyOfGame(arr,n)) # 17

# Method 2: Recursion + Memoization, TC: O(n^2)


def optimalStrategyOfGame(arr, n):

	table = [[0 for i in range(n)]
			for i in range(n)]

	for gap in range(n):
		for j in range(gap, n):
			i = j - gap

			x = 0
			if((i + 2) <= j):
				x = table[i + 2][j]
			y = 0
			if((i + 1) <= (j - 1)):
				y = table[i + 1][j - 1]
			z = 0
			if(i <= (j - 2)):
				z = table[i][j - 2]
			table[i][j] = max(arr[i] + min(x, y),
							arr[j] + min(y, z))
	return table[0][n - 1]


# Driver Code
arr1 = [2,3,15, 7]
n = len(arr1)
print(optimalStrategyOfGame(arr1, n))