import sys
from math import ceil
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    r = int(((1+4*n)**0.5-1)/2)
    if r*(r+1)<n:
        r+=1
    
    print(n+r)