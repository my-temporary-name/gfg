# Find 2 odd occuring numbers in a list
# Example: [2,2,3,2,2,4,4,4] => 3,4

# Naive approach: We can just count the number of times each number appears in the list and return the number that appears only once.

def oddAppearing(arr):
    for i in arr:
        count =0

        for j in arr:
            if i==j:
                count+=1
        if count%2!=0:
            print(i, end=" ")

if __name__ =='__main__':
    arr = [2,2,3,2,2,4,4,4]
    oddAppearing(arr)
    print()