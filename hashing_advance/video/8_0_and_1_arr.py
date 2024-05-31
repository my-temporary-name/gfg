# Longest subarray with equal number of zero and one

# naive solution: TC=O(n^2)
def longZeroSA(arr):
    n = len(arr)
    res = 0
    for i in range(n):
        c_0 = 0
        c_1 = 0

        for j in range(i,n):
            if arr[j]==0:
                c_0+=1
            else:
                c_1+=1
            if c_0 == c_1:
                res = max(res, j-i+1)
    return res

arr = [1,0,1,1,1,0,0]
print(longZeroSA(arr))

# efficient solution: TC=O(n)
# we will replace all zeros with -1 and find the longest subarray with sum=0 (done previously)


def longZeroSA2(arr):
    n = len(arr)
    for i in range(n):
        if arr[i]==0:
            arr[i]=-1
    
    mydict = dict()
    sum = 0
    maxlen = 0
    for i in range(n):
        sum+=arr[i]
        if sum==0:
            maxlen=i+1
        if sum in mydict:
            maxlen = max(maxlen, i-mydict[sum])
        else:
            mydict[sum]=i
    return maxlen

arr = [1,0,1,1,1,0,0]
print(longZeroSA2(arr))