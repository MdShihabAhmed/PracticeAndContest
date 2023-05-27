import sys

input = sys.stdin.readline

n, x = map(int,input().split())
a = list(map(int,input().split()))

prefixSum = [0]

for i in range(n):
    prefixSum.append(prefixSum[i]+a[i])

i = j = 0

result = 0
while(i<=n and j<=n):
    if prefixSum[j]-prefixSum[i]==x:
        result+=1
        i+=1
    elif prefixSum[j]-prefixSum[i]>x:
        i+=1
    else:
        j+=1

print(result)