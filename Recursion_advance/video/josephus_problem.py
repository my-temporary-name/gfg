# If n people are standing in a circle and we need to kill every kth person, then the last person standing will be the winner. This is called Josephus Problem.
# Example: n=7, k=3 ; Output: 3 ( if 0 to 6 is the index of people, then 3rd person will be the winner)

def josephus(n,k): # Time complexity: O(n) ; because we are killing every kth person and then moving to next person in circle 
    if n==1:
        return 0
    else:
#        return josephus(n-1,k) # This is wrong because this is just decrementing the number of people standing in circle. We need to kill every kth person.
        return (josephus(n-1,k)+k)%n # This is correct because we are killing every kth person and then moving to next person in circle.

print(josephus(7,3)) # 3

# What if index starts from 1 instead of 0?
def josephusBeginWithOne(n,k):
    return josephus(n,k)+1