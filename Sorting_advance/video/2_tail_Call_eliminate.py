# Tail Call Elimination in QuickSort


def qSort(arr,l,r):
    if l<r:
        p = partition(arr,l,r)
        qSort(arr,l,p)
        qSort(arr,p+1,r)

# Tail call optimization

def qSort(arr,l,r):
    while l<r:
        p = partition(arr,l,r)
        qSort(arr,l,p)
        l=p+1