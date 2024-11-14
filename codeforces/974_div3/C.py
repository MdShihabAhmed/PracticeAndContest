import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    if n<3:
        print(-1)
        continue
    a.sort()
    s = sum(a)
    avg = s/(n*2)
    i = n//2
    print(max(((a[i]*n*2)+1)-s,0))
