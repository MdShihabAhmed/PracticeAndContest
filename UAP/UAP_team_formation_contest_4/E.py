import sys

input = sys.stdin.readline

def bfs(graph, source, m, n):
    queue = []
    queue.append(source)
    a, b, c = 0, 0, 0
    cnt = 0
    valid = {'a','b','c','.'}
    while(queue):
        temp = queue.pop(0)
        cnt+=1
        if not a and graph[temp[0]][temp[1]]=='a':
            a = cnt
        elif not b and graph[temp[0]][temp[1]]=='b':
            b = cnt
        elif not c and graph[temp[0]][temp[1]]=='c':
            c = cnt
        graph[temp[0]][temp[1]] = 'h'
        if temp[0]-1>=0 and graph[temp[0]-1][temp[1]] in valid:
            queue.append((temp[0]-1,temp[1]))
        if temp[0]+1<m and graph[temp[0]+1][temp[1]] in valid:
            queue.append((temp[0]+1,temp[1]))
        if temp[1]-1>=0 and graph[temp[0]][temp[1]-1] in valid:
            queue.append((temp[0],temp[1]-1))
        if temp[1]+1<n and graph[temp[0]][temp[1]+1] in valid:
            queue.append((temp[0],temp[1]+1))
        print(a,b,c)
    return max(a,b,c)

for _ in range(int(input())):
    m, n = map(int,input().split())
    graph = []
    h = [0, 0]
    flag = True
    for i in range(m):
        temp = input().rstrip()

        graph.append([])
        for c in range(n):
            graph[i].append(temp[c])
        if flag:
            for j in range(n):
                if graph[i][j] == 'h':
                    h = (i, j)
                    flag = False
                    break
    print(h)
    print("Case ",_+1,": ",bfs(graph,h,m,n),sep="")