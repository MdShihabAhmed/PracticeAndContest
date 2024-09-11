import sys

input = sys.stdin.readline

n = int(input())
cond = [0]
taste = [0]
for i in range(n):
    x, y = map(int,input().split())
    cond.append(x)
    taste.append(y)

dp = [[0]*(n+1) for i in range(2)]
for i in range(1,n+1):
    if cond[i]:
        dp[1][i]+= max(taste[i]+dp[0][i-1],dp[1][i-1])
        dp[0][i]=dp[0][i-1] 
    else:
        dp[0][i]+= max(taste[i]+dp[0][i-1],taste[i]+dp[1][i-1],dp[0][i-1])
        dp[1][i]=dp[1][i-1] 

# print(dp[0])
# print(dp[1])
print(max(dp[0][n],dp[1][n]))