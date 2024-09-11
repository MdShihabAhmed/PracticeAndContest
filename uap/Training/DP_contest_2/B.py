import sys

input = sys.stdin.readline

n, k = map(int,input().split())
a = list(map(int,input().split()))

dp = [[0]*(k+1) for i in range(n+1)]
dp1 = [[0]*(k+1) for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        
