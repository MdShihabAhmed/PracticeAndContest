import sys

input = sys.stdin.readline

def solver(n, W, weight, value):
    dp = [[0 for i in range(W+1)] for j in range(n+1)]

    for i in range(1,n+1):
        for j in range(1, W+1):
            if weight[i-1]>j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],value[i-1]+dp[i-1][j-weight[i-1]])
    
    return dp[-1][-1]

for _ in range(1):
    n, W = map(int,input().split())
    weight = [0 for _ in range(n)]
    value = [0 for _ in range(n)]
    
    for i in range(n):
        weight[i], value[i] = list(map(int,input().split()))

    print(solver(n, W, weight, value))