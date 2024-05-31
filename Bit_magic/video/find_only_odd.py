#  In a list all the number are even except one number, find that number.
# Example: [2,2,3,2,2] => 3

# Naive approach: We can just count the number of times each number appears in the list and return the number that appears only once.

l = [10, 20, 30, 20 ,10]

for x in l:
    count = l.count(x)
    if count%2!=0:
        print(x)
        break


# Method 2: Using XOR operator

res =0
for x in l:
    res = res ^ x

print(res) # 30

# l = [10, 20, 30, 20 ,10]
# res = 0
# x =10, res = 0 ^ 10 = 10
# x =20, res = 10 ^ 20 = 30
# x =30, res = 30 ^ 30 = 0
# x =20, res = 0 ^ 20 = 20
# x =10, res = 20 ^ 10 = 30
# res = 30

# 10 ^ 20 ^ 30 ^ 20 ^ 10 = 30 (as XOR of two same numbers is 0, so only the number that appears once will be left in the end.)