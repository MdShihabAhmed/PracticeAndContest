import sys
from bisect import bisect_left

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    # b.sort()
    bor = []
    for i in range(1,n):
        if a[i]>a[0]:
            bor.append(a[i])
    bor.sort()
    result = []
    for i in range(m):
        if b[i]<=a[0]:
            result.append(1)
            continue

        temp = len(bor)-bisect_left(bor,b[i])

        result.append(temp+1)

    result.sort()
    finalResult = []
    for i in range(m):
        temp = 0
        for j in range(i,m,i+1):
            temp+=result[j]
        finalResult.append(temp)
    
    print(" ".join(map(str,finalResult)))

    