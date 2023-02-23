import sys
from collections import defaultdict

input = sys.stdin.readline

def bipart(graph, n):
    visited = [False]*(n+1)
    index = [-1]*(n+1)
    
    index[1] = 0
    
    stack = [1]
    visited[1] = True
    while(stack):
        temp = stack.pop()
        for child in graph[temp]:
            if not visited[child]:
                stack.append(child)
                visited[child] = True
                if not index[temp]:
                    index[child] = 1
                else:
                    index[child] = 0
    u = 0
    v = 0
    for i in range(n+1):
        if index[i]==0:
            u+=1
        elif index[i]==1:
            v+=1
    return (u*v-n+1)

n = int(input())
graph = defaultdict(list)
for i in range(n-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bipart(graph,n))