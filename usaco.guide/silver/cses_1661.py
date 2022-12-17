import sys
from collections import defaultdict

input = sys.stdin.readline

n, x = map(int,input().split())
a = list(map(int,input().split()))

prefixSum = [0]*(n+1)

similar = defaultdict(int)
similar[0] = 1

result = 0
for i in range(n):
    prefixSum[i+1] = (prefixSum[i]+a[i])

    result+= similar[prefixSum[i+1]-x]
    similar[prefixSum[i+1]] += 1

print(result)
