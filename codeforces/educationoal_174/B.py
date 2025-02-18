import sys
from collections import Counter

input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    c = list(map(int,input().split()))
    c = Counter(c)
    cnt = []
    for val in c.values():
        cnt.append(val)
    
    one = 0
    for v in cnt:
        if v==1:
            one+=1
    
    result = ((one+1)//2)*2
    result+= (len(cnt)-one)
    print(result)
