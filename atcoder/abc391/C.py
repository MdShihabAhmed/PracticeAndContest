n, q = map(int,input().split())
nest = [1]*(n+1)
pigeon = [i for i in range(n+1)]

result = 0
for i in range(q):
  query = list(input().split())
  if query[0]=="1":
    p = int(query[1])
    h = int(query[2])
    current = pigeon[p]
    nest[current]-=1
    if nest[current]==1:
      result-=1
    pigeon[p]=h
    nest[h]+=1 
    if nest[h]==2:
      result+=1
  else:
    print(result)