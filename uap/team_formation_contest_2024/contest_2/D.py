import sys

input = sys.stdin.readline

n, m = map(int,input().split())

pre = [0]
t = list(map(int,input().split()))
for i in range(n):
    pre.append(pre[i]+t[i])

result = 0
for i in range(m):
    a, b = map(int,input().split())
    result+=pre[b]-pre[a-1]

print(result)