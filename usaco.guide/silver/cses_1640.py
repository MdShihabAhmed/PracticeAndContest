import sys

input = sys.stdin.readline

n, x = map(int,input().split())
a = list(map(int,input().split()))

indexedA = []
for i in range(n):
    indexedA.append([a[i], i+1])

indexedA.sort()

l = 0
r = n-1

while l<r:
    temp = indexedA[l][0] + indexedA[r][0]

    if temp==x:
        print(indexedA[l][1],indexedA[r][1])
        break
    elif temp<x:
        l+=1
    else:
        r-=1

if l==r:
    print("IMPOSSIBLE")


