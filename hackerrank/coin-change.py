import sys

input = sys.stdin.readline

def solver(n, m, c):
    solveChart = [[0]*(n+1)]*(m+1)
    c.sort()
    for i in range(m):
        for j in range(n):
            solveChart[i][j]=
    print(solveChart)

for _ in range(1):
    n, m = map(int,input().split())
    c = list(map(int,input().split()))

    print(solver(n, m, c))