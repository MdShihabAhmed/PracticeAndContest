import sys
from collections import defaultdict

input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    pre = [0]
    for i in range(n):
        pre.append(pre[i]+a[i])
    track = dict()
    result = 0
    last = -1
    for i in range(n+1):
        if str(pre[i]) in track:
            if track[str(pre[i])]>=last:
                result+=1
                last = i
        track[str(pre[i])] = i
    
    print(result)
        
