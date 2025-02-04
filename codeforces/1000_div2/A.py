import sys

input = sys.stdin.readline

for _ in range(int(input())):
    l, r = map(int,input().split())
    if r==1:
        print(1)
        continue
    print(r-l)
    