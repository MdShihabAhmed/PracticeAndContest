import sys

input = sys.stdin.readline
def bfs(graph, source, n):
    distance = [0 for i in range(n)]
    visited = [False]*n
    queue = []

    queue.append(source)
    visited[source] = True
    while(True):
        if len(queue)==0:
            break

        for j in range(n):
            if graph[queue[0]][j]==1 and not visited[j]:
                queue.append(j)

                distance[j]+=distance[queue[0]]+1
                visited[j] = True
        queue.pop(0)
    
    return distance

for _ in range(int(input())):
    n = int(input())
    r = int(input())
    graph = [[0 for i in range(n)] for j in range(n)]

    for i in range(r):
        u, v = map(int,input().split())
        graph[u][v] = 1
        graph[v][u] = 1
    s, d = map(int,input().split())

    begin = bfs(graph, s, n)
    end = bfs(graph, d, n)
    end[s] = 0
    result = 0
    for i in range(n):
        result = max(result, begin[i]+end[i])
    
    print(f"Case {_+1}: {result}")


