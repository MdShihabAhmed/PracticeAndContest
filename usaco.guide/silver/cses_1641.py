import sys

input = sys.stdin.readline

n, x = map(int,input().split())
a = list(map(int,input().split()))

indexedA = []
for i in range(n):
    indexedA.append([a[i], i+1])

indexedA.sort()

flag = False

#two sum with an extra static value
for i in range(n):
    l = 0
    r = n-1
    while l<r:
        if l==i:
            l+=1
            continue
        elif r==i:
            r-=1
            continue
        temp = indexedA[l][0] + indexedA[r][0] + indexedA[i][0]
        if temp==x:
            print(indexedA[l][1],indexedA[r][1],indexedA[i][1])
            flag = True
            break
        elif temp<x:
            l+=1
        else:
            r-=1
    if flag:
        break

if not flag:
    print("IMPOSSIBLE")


