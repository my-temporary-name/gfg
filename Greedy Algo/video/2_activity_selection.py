# Activity selection problem
# Activity: (start, finish)
# Eg: [ [1,3], [2,4], [3,8], [10,11]]
# O/P: 3 i.e. [ [1,3], [3,8], [10,11]] (2nd activity is not selected because it overlaps with 1st activity)

# Idea:
# 1. Sort the activities based on the finish time
# 2. Initialize the first activity as selected
# 3. For each remaining activity, if the start time is greater than or equal to the finish time of the last selected activity, then select the activity
# 4. Return the selected activities

def MaxActivities(arr):
    n = len(arr)
    arr.sort(key = lambda x:x[1]) # sort based on finish time
    prev = 0
    res = 1

    for curr in range(1,n):
        if arr[curr][0] >= arr[prev][1]:
            res+=1
            prev = curr
    return res


arr = [[1,3], [2,4], [3,8], [10,11]]
print(MaxActivities(arr)) # 3
