# Job Sequencing Problem
# Given an array of jobs where every job has a deadline and associated profit if the job is finished before the deadline. 
# It is also given that every job takes a single unit of time, so the minimum possible deadline for any job is 1. 
# How to maximize total profit if only one job can be scheduled at a time.

# 1. Short job in decreasing order of profit
# 2. Add the jobs to the latest possible time slot
# 3. If job can't be added, ignore the job

def printJobScheduling(arr,t):
    n = len(arr)
    arr.sort(key=lambda x: x[1], reverse = True)
    result = [False]*t
    res=0

    for i in range(n):
        for j in range(min(t-1, arr[i][0]-1), -1, -1):
            if result[j] == False:
                result[j]=True
                res += arr[i][1]
                break
    return res

arr=[(4,50) , (1,5) , (1,20) , (5,10) , (5,80)]
t=5
print(printJobScheduling(arr,t))
