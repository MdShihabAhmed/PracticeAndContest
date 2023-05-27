import sys
from math import ceil,sqrt

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    
    t = ceil((sqrt((13+4*n)/13)-1)/2)
    t2 = t-1
    minus = 26*(t2*(t2+1))/2
    temp = n - minus
    c = ceil(temp/t)

    print(f"Case #{_+1}: {chr(64+c)}")