import sys
from collections import defaultdict

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    p = list(map(int,input().split()))
    
    tree = defaultdict(set)
    for i in range(n-1):
        tree[str(p[i])].add(str(i+2))
    
    ranges = []
    for i in range(n):
        l, r = map(int,input().split())
        ranges.append([l,r,0])
    
    result = 0

    stack = []
    stack.append(str(1))
    visited = set()

    while(stack):
        node = stack.pop()
        if node not in visited:
            stack.append(node)
            visited.add(node)

            for v in tree[node]:
                stack.append(v)
        else:
            temp2 = 0
            for v in tree[node]:
                temp2+=ranges[int(v)-1][2]
            
            if ranges[int(node)-1][0]>temp2:
                ranges[int(node)-1][2]=ranges[int(node)-1][1]
                result+=1
                continue
            ranges[int(node)-1][2]=min(temp2,ranges[int(node)-1][1])


    print(result)