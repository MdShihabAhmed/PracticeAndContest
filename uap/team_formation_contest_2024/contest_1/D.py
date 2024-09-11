import sys

input = sys.stdin.readline

n,m,q = map(int,input().split())
coordinates = []
sweet = [[0 for i in range(m+1)] for j in range(n+1)]

for i in range(n):
    coordinates.append(list(map(int,input().split())))

for k in range(q):
    x, y = map(int,input().split())
    sweet2 = [[0 for i in range(m+1)] for j in range(n+1)]
    sweet2[x][y]=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if (i-2>=0 and j-1>=0) and coordinates[i-1][j-1]<=coordinates[i-2][j-1]:
                sweet2[i][j]+=sweet2[i-1][j]
            if (i-2>=0 and j-2>=0) and coordinates[i-1][j-1]<=coordinates[i-2][j-2]:
                sweet2[i][j]+=sweet2[i-1][j-1]
            if (i<n and j-1<m) and coordinates[i-1][j-1]<=coordinates[i][j-1]:
                sweet2[i][j]+=sweet2[i+1][j]
            if (i<n and j<m) and coordinates[i-1][j-1]<=coordinates[i][j]:
                sweet2[i][j]+=sweet2[i+1][j+1]
    for i in range(n,0,-1):
        for j in range(m,0,-1):
            if (i-2>=0 and j-1>=0) and coordinates[i-1][j-1]<=coordinates[i-2][j-1]:
                sweet2[i][j]+=sweet2[i-1][j]
            if (i-2>=0 and j-2>=0) and coordinates[i-1][j-1]<=coordinates[i-2][j-2]:
                sweet2[i][j]+=sweet2[i-1][j-1]
            if (i<n and j-1<m) and coordinates[i-1][j-1]<=coordinates[i][j-1]:
                sweet2[i][j]+=sweet2[i+1][j]
            if (i<n and j<m) and coordinates[i-1][j-1]<=coordinates[i][j]:
                sweet2[i][j]+=sweet2[i+1][j+1]
    for i in range(n+1):
        for j in range(m+1):
            sweet[i][j]+=min(sweet2[i][j],1)

    for i in sweet:
        print(i)
    print()
res = [-1,-1,-1]
for i in range(1,n+1):
    for j in range(1,m+1):
        if sweet[i][j]>res[2]:
            res = [i,j,sweet[i][j]]
print(res[0],res[1],res[2])