import sys

input = sys.stdin.readline

n, x = map(int,input().split())
c = list(map(int,input().split()))
mm = 1000000000

dp = [mm for j in range(x+1)]
dp[0] = 0

for i in range(1,n+1):
    for j in range(c[i-1],x+1):
        dp[j] = min(dp[j],dp[j-c[i-1]]+1)

# print(dp)
if dp[x]==mm:
    print(-1)
else:
    print(dp[x])