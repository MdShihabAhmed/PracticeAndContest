import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, x = map(int,input().split())
    if x%2:
        result = [n]*n
        result[-1]-=1
        print(*result)
    else:
        result = [n-1]*n
        result[n-2]+=1
        print(*result)