import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, x = map(int,input().split())
    a = list(map(int,input().split()))
    if n*x==sum(a):
        print("YES")
    else:
        print("NO")