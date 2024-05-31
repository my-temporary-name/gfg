# We have to find maximum profit we can make by buying and selling stocks.
# Example: [1,5,3,8,12] -> 13
# Buy on day 1 (price = 1) and sell on day 2 (price = 5), profit = 5-1 = 4
# Then buy on day 3 (price = 3) and sell on day 5 (price = 12), profit = 12-3 = 9
# Total profit = 4+9 = 13

# Naive approach: Time complexity: O(n^2)
# We can use maxprofit function
# x0, x1, x2, x3, x4...xi...xj...xn-1
# Consider every pair (xi,xj) such that i<j and xj>xi
# Profit with each pair is considered as: (xj-xi) + maxprofit(0,i-1)+ maxprofit(j+1, n-1)

# l = [1,5,3,8,12]
# Profit with pair (1,5) = 4 + 0 + 9 = 13
# Profit with pair (1,3) = 2 + 0 + 4 = 6

def maxProfit(arr, b, e):
    if(e<=b):
        return 0
    res=0
    for i in range(b, e):
        for j in range(i+1, e+1):
            if(arr[j]>arr[i]):
                curr=arr[j]-arr[i]+maxProfit(arr, 0, i-1)+maxProfit(arr, j+1, e)
                res=max(res, curr)
    return res

arr=[1, 5, 3, 8, 12]
b=0
e=4
print(maxProfit(arr, b, e))

# Efficient approach: Time complexity: O(n)
# We will simply purchase at the local minima and sell at the local maxima.


l = [1,5,3,8,12]
n= len(l)
profit=0

for i in range(1,n):
    if l[i]>l[i-1]:
        profit+=l[i]-l[i-1]

print("Using 1 for loop: ",profit)