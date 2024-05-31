# Find subset of a string
# Example: s = "abc" ; Output: ["", "a", "b", "c", "ab", "ac", "bc", "abc"]

def subset_str(s, curr, index): # TC: O(2^n) , SC: O(n) ; Because each character has 2 choices, either include or not include
    if index == len(s): # Base case, when we reach end of string
        print(curr, end=" ")
        return
    subset_str(s, curr, index+1) # When we don't include current character
    subset_str(s, curr+ s[index], index+1) # when we include current character

s = "abc"
print(subset_str(s, "",0))