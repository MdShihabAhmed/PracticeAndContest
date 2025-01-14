import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int,input().split())
    print(max(n,m)+1)