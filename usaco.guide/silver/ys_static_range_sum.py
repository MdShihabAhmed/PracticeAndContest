import sys

input = sys.stdin.readline

n, q = map(int,input().split())
a = list(map(int,input().split()))

prefixSum = [0]*(n+1)
for i in range(n):
    prefixSum[i+1] = a[i]+prefixSum[i]

for i in range(q):
    l, r = map(int,input().split())
    print(prefixSum[r]-prefixSum[l])