# Generate first n numbers with the given digit 
# Eg: n=[5,6] , k= 10 : [5,6,55,56,65,66,555,556,565,566]

from collections import deque

def printFirstN(n):
    q = deque()
    q.append("5")
    q.append("6")

    for i in range(n):
        curr = q.popleft()
        print(curr, end=" ")
        q.append(curr + "5")
        q.append(curr + "6")

printFirstN(10) # 5 6 55 56 65 66 555 556 565 566