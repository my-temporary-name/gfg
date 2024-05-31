# check for palindrome Permutation
# rearrange the characters of a string to make it a palindrome.

# example: geek --> False
#          aabb --> True

# Naive soln: To generate all strings and check if any of them is palindrome.: TC=O(n! x n)

# Efficient solution: TC = O(n)
# Answer is going to be true if there is at most one character with odd frequency.


from collections import Counter
# work of counter is to count the frequency of each character in the string. and return a dictionary.

def isPalPer(arr):
    cnt = Counter(arr)
    odd = 0
    for freq in cnt.values():
        if freq%2!=0:
            odd+=1
            if odd>1:
                return False
    return True

arr = "aabb"
print(isPalPer(arr))

arr = "geek"
print(isPalPer(arr))