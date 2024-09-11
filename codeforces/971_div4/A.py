import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a,b = map(int,input().split())
    r = float('inf')
    for c in range(a,b+1):
        r = min((c-a)+(b-c),r)
    
    print(r)
    