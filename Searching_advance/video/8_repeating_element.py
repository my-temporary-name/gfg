# Repeating Element: In a array find the element which is repeating more than one. No other element should be repeating more than once.

# Example [0,2,1,3,2,2]; Output: 2

# Rules:
# 1. Only one element should be repeating more than once.
# 2. Array size is n>=2
# 3. All elements from 0 to max(arr) should be present in the array. therefor 0<max(arr)<=n-2

# Naive Approach: Time Complexity: O(n^2)

arr=[0,2,1,3,2,2]

for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            print("Repeating element is: ",arr[i])
        break

# Another Approach is sort the array and then find the repeating element. Time Complexity: O(nlogn)
# if arr[i]==arr[i+1]: print("Repeating element is: ",arr[i])

# Efficient Approach: Time Complexity: O(n), space Complexity: O(n)

def repeat(arr,n):
    visit = [False]*n
    for i in range(n):
        if visit[arr[i]]:
            return arr[i]
        visit[arr[i]]=True
    return -1

# arr=[0,2,1,3,2,2]
arr=[1,3,2,4,3,3]
n= len(arr)
print("Repeating element is : ",repeat(arr,n)) # Output: 2