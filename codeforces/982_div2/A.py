import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    x = float('-inf')
    y = float('-inf')
    for i in range(n):
        a,b = map(int,input().split())
        x = max(a,x)
        y = max(b,y)
    print(2*(x+y))
    

    

    