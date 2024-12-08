from sys import stdin
from collections import defaultdict

graph = defaultdict(list)
points = set()
for lines in stdin:
    line = lines.split(";")
    for li in line:
        li = li.strip()
        if not li:
            continue
        li = li.split("),(")
        first = li[0]+")"
        second = "("+li[1]
        graph[first].append(second)
        graph[second].append(first)
        points.add(first)
        points.add(second)

visited = set()
polygons = 0
figures = 0
for point in  points:
    if point in visited:
        continue
    figures+=1
    
    stack = [point]
    visited.add(point)
    
    flag = True

    while(stack):
        p = stack.pop()

        if len(graph[p])!=2:
            flag = False
        for node in graph[p]:
            if node in visited:
                continue
            stack.append(node)
            visited.add(node)

    
    if flag:
        polygons+=1

print(figures,polygons)
