import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n,m = map(int,input().split())
    s = input().strip()
    grid = []
    for i in range(n):
        grid.append(list(map(int,input().split())))
    
    i = 0
    j = 0
    for k in range(n+m-2):
        su = 0
        if s[k]=="D":
            for l in range(m):
                su+=grid[i][l]
            grid[i][j]=(-su)
            i+=1
        else:
            for l in range(n):
                su+=grid[l][j]
            grid[i][j]=(-su)
            j+=1
    su1 = 0
    for l in range(m):
        su1+=grid[n-1][l]
    grid[n-1][m-1]=-su1
    
        
    for i in range(n):
        print(*grid[i])


        