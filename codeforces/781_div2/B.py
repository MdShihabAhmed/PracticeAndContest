import sys
from collections import Counter
input = sys.stdin.readline

def solver(n,a):
    a.sort(key=lambda x:x[1])
    last = a[-1][1]
    modify = n-last
    result = 0
    while(modify):
        result+=1
        m=min(modify,last)
        result+=m
        modify-=m
        last+=m
    print(result)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a = Counter(a)
    la = list(map(lambda x:[x[0],x[1]],a.items()))

    solver(n,la)