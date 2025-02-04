import sys

input = sys.stdin.readline

n, m = map(int,input().split())
a = 10000
b = -1
c = 10000
d = -1
grid = []
for i in range(n):
    s = list(input().strip())
    grid.append(s)

    for j in range(m):

        if grid[i][j]=="#":
            a = min(i,a)
            b = max(i,b)
            c = min(j,c)
            d = max(j,d)

flag = True
for i in range(a,b+1):
    for j in range(c,d+1):
        if grid[i][j]==".":
            flag = False
            break
    if not flag:
        break

if flag:
    print("Yes")
else:
    print("No")