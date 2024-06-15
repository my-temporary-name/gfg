# Minimum Coins to make a given sum
# Given a sum, we need to find the minimum number of coins required to make that sum.
# Eg: coins = [1,2,5], sum = 11
# Output: 3 (5+5+1)


def mCoins(coins,val):
    if val==0:
        return 0
    
    n = len(coins)
    res = -1

    for i in range(n):
        if coins[i]<=val:
            sub_res = mCoins(coins, val-coins[i]) # recursive call to find the minimum number of coins required to make the remaining sum
            if sub_res!=-1: # if the remaining sum can be made
                if res == -1 or sub_res+1 < res: # if the current result is better than the previous result then update the result
                    res = sub_res+1
    return res

coins = [1,2,5]
val = 11
print(mCoins(coins,val)) # 3