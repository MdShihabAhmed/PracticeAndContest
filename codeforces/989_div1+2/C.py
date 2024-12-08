import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
grid = [[0 for i in range(1000+5)] for j in range(1000+5)]
def check(i,j,n,m,s):
    if i<0 or j<0 or i>=n or j>=m:

        return
    if grid[i][j]=="?" or grid[i][j]=="x":
        return
    if grid[i][j]==s:
        grid[i][j]="x"
        check(i+1,j,n,m,"U")
        check(i-1,j,n,m,"D")
        check(i,j+1,n,m,"L")
        check(i,j-1,n,m,"R")
    return

for _ in range(int(input())):
    n, m = map(int,input().split())
    
    for i in range(n):
        temp = list(input().strip())
        for j in range(m):
            grid[i][j]=temp[j]
    
    for i in range(n):
        for j in range(m):
            if (i==0 and grid[i][j]=="U") or (i==n-1 and grid[i][j]=="D") or (j==0 and grid[i][j]=="L")  or (j==m-1 and grid[i][j]=="R"):
                grid[i][j]="x"
                check(i+1,j,n,m,"U")
                check(i-1,j,n,m,"D")
                check(i,j+1,n,m,"L")
                check(i,j-1,n,m,"R")

    
    result = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j]=="x":
                continue
            temp = 0
            if i<n-1 and grid[i+1][j]!="x":
                temp+=1
            if i>0 and grid[i-1][j]!="x":
                temp+=1
            if j<m-1 and grid[i][j+1]!="x":
                temp+=1
            if j>0 and grid[i][j-1]!="x":
                temp+=1
            if temp:
                result+=1
            
    print(result)
