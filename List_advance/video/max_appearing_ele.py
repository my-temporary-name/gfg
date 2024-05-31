# Maximum Appearing Element in Ranges
# Example: l = [1, ,2 5,15] & r = [5,8,7,18] ; Output: 5
# [1,2,3,4,5] ; [2,3,4,5,6,7,8]; [5,6,7] ; [15,16,17,18] These are the arrays in above ranges (l[i],r[i])

# Naive Approach: Time Complexity: O(n*max) where max is the maximum value allowed, here it is 100. n is size of l or r

def maxAppear(l,r):
    freq = [0]*100
    for i in range(len(l)):
        for j in range(l[i], r[i]+1):
            freq[j]+=1
    return freq.index(max(freq))

l=[1,2,5,15]
r=[5,8,7,18]
print("Maximum appearing element is: ",maxAppear(l,r)) # Output: 5


# Efficient Approach: Time Complexity: O(n + Max) where n is size of l or r and Max is the maximum value allowed, here it is 100

def maxAppear(l,r):
    freq = [0]*101
    for i in range(len(l)):
        freq[l[i]]+=1
        freq[r[i]+1]-=1
    
    # freq = [0,1,1,0,1,-1,-1,0,...0]
    
    for i in range(1,100):
        freq[i] = freq[i]+freq[i-1] # prefix sum
    
    return freq.index(max(freq))

l=[1,2,5,15]
r=[5,8,7,18]
print("Maximum appearing element is: ",maxAppear(l,r)) # Output: 5