import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, q = map(int,input().split())
    p = list(map(int,input().split()))
    s = input().strip()
    
    needed = 0
    for i in range(n):
        if p[i]>i+1:
            needed+=(p[i]-i-1)
    print(needed)
    for i in range(q):
        index = int(input())

        
    print()