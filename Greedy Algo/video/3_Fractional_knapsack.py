# Fractional Knapsack Problem
# In Fractional Knapsack, we can break items for maximizing the total value of knapsack. 
# This problem in which we can break an item is also called the fractional knapsack problem.

# eg: Weight: [50,20,30]
#    Value: [600,500,400]
#    Capacity: 70
#   O/P: 1140 i.e  I2 + I3 + I1 x 20/50 = 500 + 400 + 240 = 1140

# Idea:
# 1. Calculate ratio (value/weight) for each item
# 2. Sort all items by ratio in decreasing order
# 3. Initialize result as 0, curr_capacity as capacity
# 4. Do following for every item in sorted order
#  a. If the weight of the item is less than or equal to curr_capacity, add the value of the item to the result and subtract the weight of the item from curr_capacity
# b. If the weight of the item is more than curr_capacity, then add the value of the item fractionally to the result
# 5. Return the result

def fKnaps(w,arr):
    n= len(arr)
    costWeight = []
    for i in range(n):
        c,W= arr[i][0], arr[i][1]
        costWeight.append((c, W, ((c*1.0)/w))) # cost, weight, cost/weight
    
    costWeight = sorted(costWeight, key= lambda x : x[2], reverse = True)

    res = 0.0

    for curr in costWeight:
        if curr[1]<=w:
            res+=curr[0]
            w-=curr[1]
        else:
            res += curr[0]*(w/curr[1])
            break
    return res

arr = [(120,30), (100,20), (60,10)]
W = 50
print(fKnaps(W,arr)) # 1140.0