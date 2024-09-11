import sys
from math import gcd
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    r = a[0]
    for i in range(1,n):
        r = gcd(r,a[i])
    
    print(r)