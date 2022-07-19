import sys

input = sys.stdin.readline

def solver(n, x, h):
    h.sort()
    for i in range(n):
        if h[i+n]-h[i]<x:
            return 'NO'
    
    return 'YES'
for _ in range(int(input())):
    n, x = map(int,input().split())
    h = list(map(int,input().split()))

    print(solver(n, x, h))