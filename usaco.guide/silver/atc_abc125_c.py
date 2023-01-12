import sys
from math import gcd
    
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

prefixGcd = [0]*(n)
prefixGcd[0] = arr[0]
suffixGcd = [0]*(n)
suffixGcd[n-1] = arr[n-1]

for i in range(1,n):
	prefixGcd[i] = gcd(prefixGcd[i-1],arr[i])

for i in range(n-2,-1,-1):
	suffixGcd[i] = gcd(suffixGcd[i+1],arr[i])

result = max(prefixGcd[n-2],suffixGcd[1])
for i in range(1,n-1):
	result = max(result, gcd(prefixGcd[i-1],suffixGcd[i+1]))

print(result)

