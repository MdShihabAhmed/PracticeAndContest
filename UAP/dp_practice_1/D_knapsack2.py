import sys

input = sys.stdin.readline

def solver(n, W, weight, value):
    v = 10**5
    dp = [[float('inf') for i in range(v+1)] for i in range(n+1)]
    
    for i in range(n+1):
        dp[i][0]=0

    for i in range(1, n+1):
        for j in range(1, v+1):
            if j-value[i-1]<0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-value[i-1]]+weight[i-1])

    for j in range(v,-1,-1):
        if dp[-1][j] <= W:
            return j

for _ in range(1):
    n, W = map(int,input().split())
    weight = [0 for _ in range(n)]
    value = [0 for _ in range(n)]
    
    for i in range(n):
        weight[i], value[i] = list(map(int,input().split()))

    print(solver(n, W, weight, value))