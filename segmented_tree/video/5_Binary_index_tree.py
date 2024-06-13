# Binary Indexed Tree (Fenwick Tree) is a data structure that can efficiently update elements and calculate prefix sums in a table of numbers.
# 1. used for fixed input array and multiple queries of following types:
#     a. update an element
#     b. Prefix operations( sum, product, or, xor, etc)
# 2. It is actually an array but the concept is Tree based
# 3. requires o(nlogn) preprocessing time and o(n) space.


# Every Number can be represented as sum of powers of 2
# eg: 14 = 2^3 + 2^2 + 2^1
# 9 = 2^3 + 2^0
# getSum(13): sum of number from arr[0] to arr[13] (Total 14 elements)
#           = 2^3 elements + 2^2 elements + 2^1 elements i.e arr[0-7] + arr[8-11] + arr[12-13]

# GET SUM:
# arr= [10,20,30,40,50,60,70,80,90,100]
# btTree = [0,10,30,30,100,50,110,70,360,90,190] # first element is always 0

# getSum(5) = arr[0-3] + arr[4-5]  i.e to get sum of 6 elements we use 2^2 + 2^1 i.e 4 and 2 elements
# getSum(5) = btTree[4] + btTree[6] = 100 + 110 = 210


# btTree[0] is sum of 0 elements
# btTree[1] is sum of 1 elements
# btTree[2] is sum of 2 elements
# btTree[4] is sum of first 4 elements in arr
# btTree[8] is sum of first 8 elements in arr
# ........



# https://www.geeksforgeeks.org/batch/ds-with-python/track/DSASPPY-Segment-Trees/video/MTk0OA%3D%3D
# Refer this link for clear understanding of Binary Indexed Tree