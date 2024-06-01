# Meeting the Maximum Number of Guests
# You are given a list of intervals representing the arrival and departure times of guests at a party. 
# You are also given an integer k, which represents the maximum number of guests that can be at the party at any given time. 
# Return the maximum number of guests that can be at the party at the same time.

# Example: arivals = [900, 940 ] , departures = [1000, 1030], Output: 2 # 2 guests at b/w 940 to 1000

# Idea for efficient solution: TC = O(nlogn) SC = O(1)
# Consider all events in sorted order and count the number of guests at any time.

def maxGuests(arv,dept):
    arv.sort()
    dept.sort()
    n = len(arv)
    i,j = 1,0
    curr, res = 1,1
    while i<n and j<n:
        if arv[i] <= dept[j] :
            curr+=1
            i+=1
        else:
            curr-=1
            j+=1
        res = max(res, curr)
    return res

arv = [900, 600, 700]
dept = [1000, 800, 730]
print(maxGuests(arv,dept)) # 2