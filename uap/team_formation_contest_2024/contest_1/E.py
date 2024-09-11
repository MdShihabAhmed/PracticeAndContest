import sys

input = sys.stdin.readline

n, k = map(int,input().split())
a = list(map(int,input().split()))

result = sum(a)
a.sort()
for i in range(n-k,n):
    result+=a[i]

print(result)
