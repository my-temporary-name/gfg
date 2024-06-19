# Print all the Divisors of n

# Brute force approach, TC: O(n), SC:O(n)

n =12
arr =list()

for i in range(1,n+1):
    if n%i==0:
        arr.append(i)

print(arr)

# Optimal Approach, TC: O(sqrt(n)), SC:O(1)

import math
n = 12
arr = list()


for i in range(1,int(math.sqrt(n))+1):
    if n%i==0:
        arr.append(i)
        if n//i not in arr:
            arr.append(n//i)

print(arr)
#--------------------------------------------------------------------------------------------------------
# Given a positive integer N., The task is to find the value of Σi from 1 to N F(i) where function F(i) for the number i is defined as the sum of all divisors of i.


# Example 1:

# Input:
# N = 4
# Output:
# 15
# Explanation:
# F(1) = 1
# F(2) = 1 + 2 = 3
# F(3) = 1 + 3 = 4
# F(4) = 1 + 2 + 4 = 7
# ans = F(1) + F(2) + F(3) + F(4)
#     = 1 + 3 + 4 + 7
#     = 15

# The logic to make it fast with python solution

# We start with a loop that goes through the numbers from 1 to N, i.e. i takes values from 1 to N.
# In each of these iterations, we want to find the maximum integer k that is less than or equal to N/i. 
# This integer k gives us the number of times that i fits into N without exceeding N. 
# That is, if i exactly divides N, then k will be 1, because only once does i fit into N.
# For example, if N = 10 and i = 3, then N // i is 3, since 3 fits three times in 10. 
# Thus, k will be 3, i.e. i can be added three times to the sum.
# To summarize, the line k = N // i helps to calculate the number of times a number i can be added to the total sum of the divisors. 
# This allows the sum to be calculated without the use of nested loops, and this is the algebraic approach that helps optimize the code.


N=4
if N <= 0:
  print(0)
div_sum = 0
    
for i in range(1, N + 1):
  k = N // i
  div_sum += i * k

print(div_sum)