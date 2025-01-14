import sys
from collections import Counter
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    d = []
    a = Counter(a)
    for value in a.values():
        d.append(value)
    d.sort()
    result = len(a)
    for i in range(len(d)-1):
        if d[i]<=k:
            result-=1
            k-=d[i]
    print(result)