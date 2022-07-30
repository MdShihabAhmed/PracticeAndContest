import sys
from collections import defaultdict

input = sys.stdin.readline

def bicolor(graph, n):
    color = [0]*(n+1)
    stack = []
    for i in range(1,n+1):
        if not color[i]:
            stack = [i]
            color[i] = 1
            while(stack):
                temp = stack[-1]
                for child in graph[temp]:
                    if color[child]==color[temp]:
                        print('IMPOSSIBLE')
                        return
                    if not color[child]:
                        stack.append(child)
                        if color[temp]==1:
                            color[child] = 2
                        else:
                            color[child] = 1
                        break
                else:
                    stack.pop()
    print(' '.join([str(color[i]) for i in range(1,n+1)]))
            
  

n, m = map(int,input().split())

graph = defaultdict(list)

for _ in range(m):
  a, b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)
bicolor(graph, n)

