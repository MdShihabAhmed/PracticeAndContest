import sys
from collections import defaultdict

input = sys.stdin.readline

def dfs(graph, n, c):
    visited = [False]*(n+1)
    result = 0
    for i in range(1, n+1):
        tempC = 0
        if not visited[i]:
            tempC = c[i-1]
            stack = [i]
            visited[i] = True
            while(stack):
                temp = stack.pop()
                for child in graph[temp]:
                    if not visited[child]:
                        stack.append(child)
                        visited[child] = True
                        tempC = min(tempC,c[child-1])
        result+=tempC
    return result
n, m = map(int,input().split())
c = list(map(int,input().split()))
graph = defaultdict(list)
for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

print(dfs(graph,n,c))