import sys
sys.setrecursionlimit(15000)
input = sys.stdin.readline
grid = [[0 for i in range(1000+5)] for j in range(1000+5)]
def check(i,j,n,m):
    if i<0 or j<0 or i>=n or j>=m:
        return
    if grid[i][j]=="?" or grid[i][j]=="x":
        return
    if grid[i][j]=="U":
        if i==0 or grid[i-1][j]=="x":
            grid[i][j]="x"
            if i<n-1:
                check(i+1,j,n,m)
            # if i>0:
            #     check(i-1,j,n,m)
            if j<m-1:
                check(i,j+1,n,m)
            if j>0:
                check(i,j-1,n,m)
            return
    elif grid[i][j]=="D":
        if i==n-1 or grid[i+1][j]=="x":
            grid[i][j]="x"
            # if i<n-1:
            #     check(i+1,j,n,m)
            if i>0:
                check(i-1,j,n,m)
            if j<m-1:
                check(i,j+1,n,m)
            if j>0:
                check(i,j-1,n,m)
            return
    elif grid[i][j]=="L":
        if j==0 or grid[i][j-1]=="x":
            grid[i][j]="x"
            if i<n-1:
                check(i+1,j,n,m)
            if i>0:
                check(i-1,j,n,m)
            if j<m-1:
                check(i,j+1,n,m)
            # if j>0:
            #     check(i,j-1,n,m)
            return
    elif grid[i][j]=="R":
        if j==m-1 or grid[i][j+1]=="x":
            grid[i][j]="x"      
            if i<n-1:
                check(i+1,j,n,m)
            if i>0:
                check(i-1,j,n,m)
            # if j<m-1:
            #     check(i,j+1,n,m)
            if j>0:
                check(i,j-1,n,m)
            return

for _ in range(int(input())):
    n, m = map(int,input().split())
    
    for i in range(n):
        temp = list(input().strip())
        for j in range(m):
            grid[i][j]=temp[j]
    
    for i in range(n):
        for j in range(m):
            check(i,j,n,m)
    
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
