n, w = map(int,input().split())

grid = [[] for i in range(w+1)]
for i in range(n):
  x, y = map(int,input().split())
  grid[x].append([y,i+1])

for i in range(w+1):
  grid[i].sort()


result = [-1]*(n+1)
for j in range(10**9+1):
  flag = True
  temp = 0
  for i in range(1,w+1):
    if len(grid[i])<=j:
      flag = False
      break
    temp = max(temp,grid[i][j][0])
  if not flag:
    break
  for i in range(1,w+1):
    result[grid[i][j][1]]=temp

for i in range(int(input())):
  t, a = map(int,input().split())
  if result[a]==-1:
    print("Yes")
  elif result[a]>t:
    print("Yes")
  else:
    print("No")


