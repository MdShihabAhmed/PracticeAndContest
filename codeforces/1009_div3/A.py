import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k, p = map(int,input().split())
    k = abs(k)
    temp = (k+p-1)//p
    if (n>=temp):
        print(temp)
    else:
        print(-1)