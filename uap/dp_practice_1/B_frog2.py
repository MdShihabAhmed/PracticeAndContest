import sys

input = sys.stdin.readline

def solver(n, k, height):
    dp = [0]*n
    for i in range(1, n):
        temp = float('inf')
        for j in range(i-1,max(i-k,0)-1,-1):
            temp = min(temp, abs(height[i]-height[j])+dp[j])
        dp[i] = temp
    return dp[-1]

for _ in range(1):
    n, k = map(int,input().split())
    height = list(map(int,input().split()))

    print(solver(n, k, height))