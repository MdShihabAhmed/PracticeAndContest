import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    x,y = map(int,input().split())
    d = min(x,y)
    print((n+d-1)//d)
    