import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    if n==1 or n==3:
        print(-1)
        continue
    if n&1:
        print((n-4)*"3"+(1*"6366"))
    else:
        print((n//2-1)*"33"+(1*"66"))