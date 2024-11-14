import sys
from bisect import bisect_left,bisect_right

input = sys.stdin.readline


for _ in range(1):
    n, k, q = map(int,input().split())
    countryByRegions = [[] for i in range(k)]
    
    for i in range(n):
        temp = list(map(int,input().split()))

        for j in range(k):
            countryByRegions[j].append(temp[j])
    
    for i in range(k):
        tt = countryByRegions[i][0]
        for j in range(n):
            tt = tt|countryByRegions[i][j]
            countryByRegions[i][j] = tt

    # print(countryByRegions)
    
    for i in range(q):
        m = int(input())
        ma = n-1
        mi = 0
        for j in range(m):
            r,o,c = input().split()
            r = int(r)
            c = int(c)
            if o=='<':
                t = bisect_left(countryByRegions[r-1],c)-1
                ma = min(ma,t)
            else:
                t = bisect_right(countryByRegions[r-1],c)
                mi = max(mi,t)
            # print(t)
            # print(mi,ma)    
        if mi>ma:
            print(-1)
        else:
            print(mi+1)