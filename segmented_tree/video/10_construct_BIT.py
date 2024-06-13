# Construct a Binary Indexed Tree (Fenwick Tree) from a given array

arr=[10, 20, 30, 40, 50]
n=len(arr)
bITree=[0]*(n+1)

def update(i, x):
    i=i+1 
    while(i<=n):
        bITree[i]+=x 
        i=i+(i&(-i))
        

for i in range(n):
    update(i, arr[i])
    
print(bITree)
