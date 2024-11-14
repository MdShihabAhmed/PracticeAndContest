import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    aa = sum(a)
    mi = aa%2
    ma = aa
    if ma>n:
        ma = n-(ma-n)
    print(mi,ma)