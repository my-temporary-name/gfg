# Introduction to Greedy Algorithm
# Greedy Algorithm is an algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most immediate benefit.
# Greedy algorithms are used for optimization problems. An optimization problem can be solved using Greedy if the problem has the following property:
# At every step, we can make a choice that looks best at the moment, and we get the optimal solution of the complete problem.
# If a Greedy Algorithm can solve a problem, then it generally becomes the best method to solve that problem as the Greedy algorithms are in general more efficient than other techniques like Dynamic Programming.

# 1. Find minimum number of coins that make a given value


def min_coins(coins, amt):
    coins.sort(reverse=True) # sort the coins in descending order
    res = 0
    for x in coins:
        if x<=amt:
            c=amt//x
            print(c, x)
            res+=c
            amt -= c*x
        if amt==0:
            break
    return res

coins = [5,10,2,1]
amt = 57
print(min_coins(coins, amt)) 

# General Structure of Greedy Algorithm

def get_optimal(arr):
    res = 0
    while("All items are not considered"):
        i = "select_an_item()"
        if ("feasible(i)"):
            res+=i
    return res

# Standard Problems on Greedy Algorithm
# 1. Activity Selection Problem
# 2. Fractional Knapsack Problem
# 3. Huffman Coding
# 4. Job Sequencing Problem
# 5. Prim’s Minimum Spanning Tree
# 6. Kruskal’s Minimum Spanning Tree
# 7. Dijkstra’s Shortest Path

# Finding close to optimal solution
# 1. Travelling Salesman Problem
# 2. NP-Hard Problems