import sys

input = sys.stdin.readline

# Binary Search in python


def binarySearch(array, x, low, high):

    k = -1
    while low <= high:

        mid = low + (high - low)//2

        if x >= array[mid]:
            k = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return k
def binarySearch2(array, x, low, high):

    k = -1
    while low <= high:

        mid = low + (high - low)//2

        if x <= array[mid]:
            k = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return k

for _ in range(int(input())):
    n,m,q = map(int,input().split())
    b = list(map(int,input().split()))
    a = list(map(int,input().split()))

    b.sort()

    
    for i in range(q):
        lo = binarySearch(b,a[i]-1,0,m-1)
        up = binarySearch2(b,a[i]+1,0,m-1)
        
        if up==-1:
            print(n-b[-1])
        elif lo==-1:
            print(b[0]-1)
        else:
            print((b[up]-b[lo])//2)
