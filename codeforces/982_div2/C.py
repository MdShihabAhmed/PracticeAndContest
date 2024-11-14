import sys
from collections import defaultdict
from collections import deque

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    for nex in graph[start] - visited:
        dfs(graph, nex, visited)
    return visited

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    
    graph = defaultdict(list)

    for i in range(1,n):
        graph[str(a[i]+i)].append(str(a[i]+i+i))
        
    
    stack = deque()
    stack.append(str(n))
    visited = set()
    visited.add(str(n))

    need = n
    temp = 0

    while(stack):
        top = stack.popleft()

        for node in graph[top]:
            if node in visited:
                continue
            need = max(need,int(node))
            visited.add(node)
            stack.append(node)


    print(need)
    