import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, a, b = map(int,input().split())
    if (abs(a-b)-1)%2:
        print("YES")
    else:
        print("NO")
