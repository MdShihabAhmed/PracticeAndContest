import sys
from collections import defaultdict
input = sys.stdin.readline

for _ in range(int(input())):
    n, q = map(int,input().split())
    x = list(map(int,input().split()))
    k = list(map(int,input().split()))
    d = defaultdict(int)
    
    for i in range(n):
        d[(i*(n-i-1))+(n-1)]+=1
        if i<n-1:
            d[((i+1)*(n-i-1))]+=(x[i+1]-x[i]-1)
    
    result = []
    for i in range(q):
        result.append(d[k[i]])
    print(" ".join(map(str,result)))