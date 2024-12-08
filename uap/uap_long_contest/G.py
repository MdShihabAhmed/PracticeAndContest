import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n,m = map(int,input().split())
    grid = []
    for i in range(n):
        temp = list(map(int,input().split()))
        grid.append(temp)
    
    if (n+m-1)%2:
        print("NO")
        continue
    dp = [[[0,0] for j in range(m)] for i in range(n)]

    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                dp[i][j]=[grid[i][j],grid[i][j]]
                continue
            if i==0:
                dp[i][j][0]=dp[i][j-1][0]+grid[i][j]
                dp[i][j][1]=dp[i][j-1][1]+grid[i][j]
                continue
            if j==0:
                dp[i][j][0]=dp[i-1][j][0]+grid[i][j]
                dp[i][j][1]=dp[i-1][j][1]+grid[i][j]
                continue

            dp[i][j][0]=max(dp[i-1][j][0],dp[i][j-1][0])+grid[i][j]
            dp[i][j][1]=min(dp[i-1][j][1],dp[i][j-1][1])+grid[i][j]

    if (dp[n-1][m-1][1]<=0 and dp[n-1][m-1][0]>=0):
        print("YES")
    else:
        print("NO")