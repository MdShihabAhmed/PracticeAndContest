import sys
from bisect import bisect_left,bisect_right

input = sys.stdin.readline


for _ in range(int(input())):
    n,d,k = map(int,input().split())
    window = [0]*(n+1)
    start = []
    for i in range(k):
        l,r = map(int,input().split())
        window[l-1]+=1
        window[r]-=1
        start.append(l-1)
    start.sort()
    
    for i in range(n):
        window[i+1]+=window[i]
    
    mi = float('inf')
    ma = float('-inf')

    bro = 0
    mom = 0
    for i in range(n-d+1):
        temp = bisect_right(start,i+d-1)-bisect_left(start,i+1)

        if window[i]+temp>ma:
            ma = window[i]+temp
            bro = i
        if window[i]+temp<mi:
            mi = window[i]+temp
            mom = i

    print(bro+1,mom+1)