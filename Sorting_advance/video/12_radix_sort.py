# Radix Sort

# counting sort is a linear time sorting algorithm that sort in O(n+k) time when elements are in range from 1 to k
# radix sort:

# 319, 212, 6, 8, 100, 50
# 1. Re-write number with leading zeros: 319, 212, 006, 008, 100, 050
# 2. Stable sort according to last digit (Least significant digit): 100, 050, 212, 006, 008, 319
# 3. Stable sort according to second last digit: 100, 006, 008, 212, 319, 050
# 4. Stable sort according to most significant digit: 006, 008, 050, 100, 212, 319