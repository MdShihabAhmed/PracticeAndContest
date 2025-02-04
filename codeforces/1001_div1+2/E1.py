import sys
from collections import defaultdict

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    w = list(map(int,input().split()))
    d = sorted(list(set(w)))
    nodes = defaultdict(set)
    for i in range(n):
        nodes[str(w[i])].add(str(i+1))
    
    graph = defaultdict(set)
    for i in range(n-1):
        u, v = input().split()
        graph[u].add(v)
        graph[v].add(u)
    
    visited = set()
    for i in range(len(d)-2,-1,-1):
        check = str(d[i])
        for j in nodes[check]:
            if j in visited:
                continue
