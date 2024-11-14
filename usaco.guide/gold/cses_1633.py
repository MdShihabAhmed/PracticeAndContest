import sys

input = sys.stdin.readline
mod = 1000000000+7
n = int(input())

dp = [0 for i in range(n+6)]
dp[5]=1
for i in range(6,n+6):
    for j in range(1,7):
        dp[i]=(dp[i]+dp[i-j])%mod

print(dp[-1])

