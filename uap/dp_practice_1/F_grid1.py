import sys

input = sys.stdin.readline

def solver(grid, h, w):
    mod = 10**9 + 7
    dp = [[0 for i in range(w+1)] for j in range(h+1)]
    dp[1][1] = 1
    for i in range(1, h+1):
        for j in range(1, w+1):
            if grid[i-1][j-1]=='.':
                dp[i][j] += (dp[i-1][j] + dp[i][j-1]) % mod

    return dp[-1][-1]

for _ in range(1):
    h, w = map(int,input().split())
    grid = []

    for i in range(h):
        grid.append(list(input().rstrip()))
    
    print(solver(grid, h, w))