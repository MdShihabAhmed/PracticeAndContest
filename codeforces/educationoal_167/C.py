import sys

input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    aa = [0 for i in range(n+1)]
    bb = [0 for i in range(n+1)]
    r = float("inf")
    aa = 0
    bb = 0
    m = 0
    for i in range(n):
        if a[i]+m>b[i]+m:
            aa+=a[i]+m
            m += a[i]
        elif a[i]+m<b[i]+m:
            bb+=b[i]+m
            m += a[i]
        elif a[i]==-1:
            m += a[i]
    

    print(min(aa,bb,m))
    

