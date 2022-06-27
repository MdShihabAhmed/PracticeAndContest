import sys

input = sys.stdin.readline

def solver(n, W, weight, value):
    dp = [0]*n
    dp = [(weight[0], value[0])]

    for i in range(1, n):
        if weight[i]+dp[i-1][0]<=W:
            dp[i][0]+=weight[i]
            dp[i][1]+=value[i]
        else:
            dp[i] = max()


for _ in range(1):
    n, W = map(int,input().split())
    weight = list(map(int,input().split()))
    value = list(map(int,input().split()))

    print(solver(n, W, weight, value))