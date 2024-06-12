# count Distinct rows in a Binary Matrix
# Given a binary matrix, we need to find the number of distinct rows in the matrix.

# Naive Approach: TC: O(r^2 * c) SC: O(r)
# 1. Initialize : res = 0
# 2. Traverse through all rows
#    a. if the current row does not match any of the previous rows, then increment res
# 3. Return res

# Efficient Approach: TC: O(r*c) SC: O(r)
# 1. Create an Empty Trie
# 2. Initialize res = 0
# 3. Do the following for each row
#   a. Consider the row as a word and insert into trie
#   b. If the row was not already present in the trie, then increment res
# 4. Return res

from collections import defaultdict

def uniqueRows(arr):
    mp = defaultdict(int) # to store the frequency of each row
    t = ""  

    for x in arr: # convert each row into a string
        t = "" # initialize t as an empty string
        for y in x: # convert each element of the row into a string
            t += y # append the element to the string
        
        mp[t] += 1 # increment the frequency of the row
    
    cnt = 0 

    for x in mp: # count the number of rows with frequency 1
        if mp[x]==1: # if the frequency of the row is 1
            cnt += 1
    
    return cnt

arr = [
		['0', '1', '1', '0'],
		['0', '1', '1', '1'],
		['0', '1', '1', '0'],
		['0', '1', '0', '0'],
	]

print(uniqueRows(arr))