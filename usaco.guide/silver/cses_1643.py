import sys

input = sys.stdin.readline

n = int(input())
x = list(map(int,input().split()))

prefixSum = [0]*(n+1)

for i in range(n):
    prefixSum[i+1] += max(prefixSum[i]+x[i],x[i])

print(max(prefixSum[1:]))
