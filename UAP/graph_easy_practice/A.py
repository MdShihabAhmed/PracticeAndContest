import sys

input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    temp = list(map(int,input().split()))
    graph.append(sorted(temp[2:]))

result = [[0, 0] for i in range(n)]

visited = [False]*n
stack = []
time = 0
start = 0
while(True):
    if not visited[start]:
        time+=1
        stack.append(start)
        result[start][0] = time
        temp = stack[-1]
        visited[start] = True
        for j in range(len(graph[temp])):
            if not visited[graph[temp][j]-1]:
                stack.append(graph[temp][j]-1)
                time+=1
                result[graph[temp][j]-1][0] = time
                visited[graph[temp][j]-1] = True
                break
    else:
        temp = stack[-1]
        for j in range(len(graph[temp])):
            if not visited[graph[temp][j]-1]:
                stack.append(graph[temp][j]-1)
                time+=1
                result[graph[temp][j]-1][0] = time
                visited[graph[temp][j]-1] = True
                break
        else:
            time+=1
            result[stack.pop()][1] = time
    if len(stack)==0:
        for b in range(n):
            if not visited[b]:
                start = b
                break
        else:
            break
    
for i in range(n):
    print(i+1,result[i][0],result[i][1])

