n, m = map(int,input().split())

s = []
for i in range(n):
  s.append(list(input()))
t = []
for i in range(m):
  t.append(list(input()))

a = 0
b = 0
for i in range(n-m+1):
  for j in range(n-m+1):
    flag = False
    for k in range(m):
      for l in range(m):
        if s[i+k][j+l]!=t[k][l]:
          flag = True
          break
      if flag == True:
        break
    
    if flag == False:
      a = i+1
      b = j+1
      break
  if a>0:
    break

print(a,b)