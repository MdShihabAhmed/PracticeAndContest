from collections import defaultdict
n = int(input())

r1 = list((input().split()))
r2 = list((input().split()))
r3 = list((input().split()))

r1d = defaultdict(list)
r2d = defaultdict(list)
r3d = defaultdict(list)

for i in range(n):
    r1d[r1[i]].append(i)
    r2d[r2[i]].append(i)
    r3d[r3[i]].append(i)

for i in range(1,n+1):
    if i in r1d and i in r2d and i in r3d:
        continue
    
