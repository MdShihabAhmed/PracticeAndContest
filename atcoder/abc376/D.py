import sys
from collections import defaultdict,deque

input = sys.stdin.readline

graph = defaultdict(list)
n, m = map(int,input().split())

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

stack = deque()
stack.append(1)

arr = [float('inf')]*(n+1)
arr[1] = 0

flag = False

while(stack):
    back = stack.popleft()
    for ver in graph[back]:
        if ver==1:
            flag = True
            arr[1] = arr[back]+1
            break
        if arr[ver]==float('inf'):
            stack.append(ver)
            arr[ver]= arr[back]+1
    if flag:
        break


if flag:
    print(arr[1])
else:
    print(-1)
