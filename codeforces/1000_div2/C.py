import sys
from collections import defaultdict

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    graph = defaultdict(set)
    for i in range(n-1):
        u, v = input().strip().split()
        graph[u].add(v)
        graph[v].add(u)
    
    print(graph)
    visited = set()
    node = ""
    children = -1
    for key, value in graph.items():
        if len(value)>=children:
            children = len(value)
            node = key
    visited.add(node)
    graph.pop(node)
    for key, value in graph.items():
        if node in value:
            graph[key].remove(node)

    print(graph)
    #second
    node = ""
    children = -1
    for key, value in graph.items():
        if len(value)>=children:
            children = len(value)
            node = key

    visited.add(node)
    graph.pop(node)
    for key, value in graph.items():
        if node in value:
            graph[key].remove(node)
    
    print(graph)
    result = 0
    for i in range(n):
        temp = str(i+1)
        if temp in visited:
            continue
        stack = [temp]
        
        result+=1
        while(stack):
            last = stack.pop()
            visited.add(last)
            for node in graph[last]:
                if node in visited:
                    continue
                stack.append(node)
                
        
    print(result)