import sys
from math import gcd

input = sys.stdin.readline

for _ in range(int(input())):
    n, a, b = map(int,input().split())
    c = list(map(int,input().split()))
    
    d = gcd(a,b)

    for i in range(n):
        c[i]%=d
    
    c.sort()

    print(c,d)