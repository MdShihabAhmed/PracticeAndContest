import sys
from collections import defaultdict
from heapq import heappop, heappush

input = sys.stdin.readline



def dijkstra(graph, start):
    n = len(graph)
    dist, parents = [float("inf")] * n, [-1] * n
    dist[start] = 0

    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if path_len == dist[v]:
            for w, edge_len in graph[v]:
                if edge_len + path_len < dist[w]:
                    dist[w], parents[w] = edge_len + path_len, v
                    heappush(queue, (edge_len + path_len, w))

    return dist, parents

for _ in range(int(input())):
    n, s1, s2 = input().strip().split()
    n = int(n)
    m1 = int(input())
    graph1 = defaultdict(set)
    for i in range(m1):
        u, v = map(int,input().split())
        u-=1
        v-=1
        graph1[str(u)].add(str(v))
        graph1[str(v)].add(str(u))
    
    m2 = int(input())
    graph2 = defaultdict(set)
    for i in range(m2):
        u, v = map(int,input().split())
        u-=1
        v-=1
        graph2[str(u)].add(str(v))
        graph2[str(v)].add(str(u))
    
    same = defaultdict(set)
    for key,value in graph1.items():
        val = value.intersection(graph2[key])
        for v in val:
            same[key].add(v)
            same[v].add(key)
    
    dist1, parents1 = dijkstra(graph1, s1)
    dist2, parents2 = dijkstra(graph2, s2)

    result = float('inf')
    for i in range(n):
        if dist