# Stock Span Problem
# Given a list of stock prices, find the span of stock's price for each day.
# Example: [13, 15, 12, 14, 16, 8, 6, 4, 10, 30]
# Output:  [1,  2,  1,  2,  5,  1, 1, 1, 4,  10] # value much be smaller or equal to the current value on the left

# Naive approach: O(n^2)

def printSpan(arr):
    for i in range(len(arr)):
        span = 1
        j=i-1
        while j>=0 and arr[i]>=arr[j]:
            span+=1
            j-=1
        print(span,end=" ")

arr = [13, 15, 12, 14, 16, 8, 6, 4, 10, 30]
printSpan(arr)

# efficient approach: O(n) , space: O(n)

# span = (index of current element)-(index of closest element on the left which is greater than the current element) # if there is greater element on the left
# else: # if there is no greater element on the left
# span = index of current element + 1
# 
# eg : [13, 15, 12, 14, 16, 8, 6, 4, 10, 30]
# span for 13 = 1
# span for 15 = 1+1 = 2
# span for 12 = 1
# span for 14 = 3-1 = 2



def PrintSpan(arr):
    st= []
    n=len(arr)
    st.append(0)
    print(1,end= " ")

    for i in range(1,n):
        while len(st)>0 and arr[st[-1]]<=arr[i]:
            st.pop()
        span = i+1 if len(st)==0 else i-st[-1]
        print(span, end=" ")
        st.append(i)

arr = [13, 15, 12, 14, 16, 8, 6, 4, 10, 30]
PrintSpan(arr)