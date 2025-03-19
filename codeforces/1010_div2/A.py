import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int,input().split())
    grid = []
    for i in range(n):
        s = input().strip()
        grid.append(s)
    
    r = c = 0
    for i in range(n):
        temp = 0
        for j in range(m):
            if grid[i][j]=='1':
                temp+=1
        r+=(temp%2)
    
    for j in range(m):
        temp = 0
        for i in range(n):
            if grid[i][j]=='1':
                temp+=1
        c+=(temp%2)
    
    print(max(r,c))