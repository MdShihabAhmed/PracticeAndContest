import sys
from collections import defaultdict

input = sys.stdin.readline
def cycle(graph, n):
    visited = [False]*(n+1)
    index = [0]*(n+1)
    
    for i in range(1,n+1):
        if not visited[i]:
            stack = [i]
            visited[i] = True
            index[i] = 1
            while(stack):
                temp = stack[-1]
                for child in graph[temp]:
                    if visited[child] and index[temp]-index[child]+1>2:
                        stack.append(stack[index[child]-1])
                        print(index[temp]-index[child]+2)
                        print(" ".join([str(stack[i]) for i in range(index[child]-1,len(stack))]))
                        return
                    if not visited[child]:
                        stack.append(child)
                        visited[child] = True
                        index[child] = len(stack)
                        break
                else:
                    stack.pop()
    print("IMPOSSIBLE")

n, m = map(int,input().split())

graph = defaultdict(list)

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
cycle(graph, n)
