import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = list(input().split())
    t = []
    for c in s:
        if len(c)==n-1:
            t.append(c)
    if t[0] == t[1][::-1]:
        print('YES')
    else:
        print('NO')

