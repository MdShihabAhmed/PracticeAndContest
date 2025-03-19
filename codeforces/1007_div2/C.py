import sys
from collections import defaultdict,deque

input = sys.stdin.readline

for _ in range(int(input())):
    n, st, en = map(int,input().split())
    tree = defaultdict(set)
    for i in range(n-1):
        u, v = input().strip().split()
        tree[u].add(v)
        tree[v].add(u)
    
    st = str(st)
    en = str(en)

    queue = deque([en])
    visited = set()
    visited.add(en)
    result = []
    while(queue):
        node = queue.popleft()
        result.append(node)
        for neighbor in tree[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    print(" ".join(result[::-1]))





