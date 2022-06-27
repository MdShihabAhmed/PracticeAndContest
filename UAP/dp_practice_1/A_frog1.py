import sys

input = sys.stdin.readline

def solver(n, height):
    dp = [0]*n
    dp[1] = abs(height[0]-height[1])
    for i in range(2,n):
        dp[i] = min(abs(height[i]-height[i-1])+dp[i-1],abs(height[i]-height[i-2])+dp[i-2])
    
    return dp[-1]

for _ in range(1):
    n = int(input())
    height = list(map(int,input().split()))

    print(solver(n, height))