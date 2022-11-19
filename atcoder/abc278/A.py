import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(*a[k:],*[0 for i in range(min(n,k))])

