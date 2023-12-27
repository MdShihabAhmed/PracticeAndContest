import sys
from math import gcd
    
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    x = list(map(int,input().split()))
    x.sort()
    result = 0
    if n==5:
        result = (max((x[-1]+x[-2])/2-(x[2]+x[0])/2, (x[-1]+x[2])/2-(x[1]+x[0])/2))
    else:
        result = ((x[-1]+x[-2])/2-(x[1]+x[0])/2)
    
    print(f"Case #{_+1}: {result}")