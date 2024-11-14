import sys

input = sys.stdin.readline


for _ in range(int(input())):
    x,y, k= map(int,input().split())
    if x>=k and y>=k:
        print(0,0,x,0)
        print(0,0,0,y)
        continue
    else:
        print(0,0,min(x,y),min(x,y))
        print(0,min(x,y),min(x,y),0)