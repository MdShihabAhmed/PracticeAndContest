import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

prefixSum = [0]*(n+1)

similar = [0]*n
similar[0] = 1

result = 0
for i in range(n):
    prefixSum[i+1] = (prefixSum[i]+a[i])%n

    result+= similar[prefixSum[i+1]]
    similar[prefixSum[i+1]] += 1

print(result)
