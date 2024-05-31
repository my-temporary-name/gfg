# Median of two sorted array
# Given two sorted arrays, a and b, find the median of two sorted arrays.
# Example: a = [1, 3, 8, 9, 15], b = [7, 11, 18, 19, 21, 25]; Output: 11

# Naive Approach: Merge the two arrays and find the median. Time Complexity: O((n+m)*log(n+m))
# 1. Create a temp array of size n+m
# 2. copy element from a,b to temp
# 3. sort the temp array
# 4. if n1+n2 is odd, return middle of temp
# 5. if n1+n2 is even, return avg of two middle elements

# Efficient Approach: Time Complexity: O(log(min(n,m)))

# Idea: let's we have 2 arrays: a1[10,20,30,40,50] and a2[5,15,25,30,35,55,65,75,85]
# 1. We will find the partition of both arrays such that left side of partition contains equal number of elements as right side using formula: floor((n1+n2+1)/2)
# 2. We will try to create 2 set for each array: left and right a1[0,i-1] and a1[i,n1-1] and a2[0,j-1] and a2[j,n2-1].
# 3. Then we will check if max(a1[i-1],a2[j-1]) <= min(a1[i],a2[j]) then we have found the partition
# 4. Median will be avg of max(a1[i-1],a2[j-1]) and min(a1[i],a2[j])


def median_of_2_arr(a1,a2):
    n1,n2=len(a1),len(a2)
    b1,e1 = 0,n1
    while(b1<=e1):
        i1 = (b1+e1)//2
        i2 = (n1+n2+1)//2 -i1
        mnr1 = float("inf") if i1==n1 else a1[i1]
        mxl1 = float("-inf") if i1==0 else a1[i1-1]

        mnr2=a2[i2]
        mxl2=a2[i2-1]

        if mxl1<=mnr2 and mxl2<=mnr1:
            if (n1+n2)%2==0:
                return (max(mxl1,mxl2)+min(mnr1,mnr2))/2
            else:
                return max(mxl1,mxl2)
        elif mxl1>mnr2:
            e1=i1-1
        else:
            b1=i1+1

a1 = [10,20,30,40,50]
a2 = [5,15,25,30,35,55,65,75,85]
print("Median of 2 sorted array is: ",median_of_2_arr(a1,a2)) # Output: 30