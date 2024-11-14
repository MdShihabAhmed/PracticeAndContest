import sys
from collections import defaultdict,deque

input = sys.stdin.readline

n, m, k = map(int,input().split())
c = list(map(int,input().split()))
paired_socks = defaultdict(list)

for i in range(m):
    l, r = input().strip().split()
    paired_socks[l].append(r)
    paired_socks[r].append(l)


visited = set()


result = 0
for i in range(n):
    if str(i+1) in visited:
        continue

    queue = deque()
    queue.append(str(i+1))
    visited.add(str(i+1))
    colors = defaultdict(int)
    colors[str(c[i])]+=1
    while(queue):
        parent = queue.popleft()

        for child in paired_socks[parent]:
            if child in visited:
                continue
            visited.add(child)
            queue.append(child)
            colors[str(c[int(child)-1])]+=1
    
    total = 0
    ma = 0
    for v in colors.values():
        ma = max(ma,v)
        total+=v

    result += (total-ma)

print(result)