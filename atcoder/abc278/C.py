import sys
from collections import defaultdict

input = sys.stdin.readline

relation = defaultdict(set)
n, q = map(int, input().split())

for i in range(q):
    t, a, b = map(int, input().split())
    if t==1:
        relation[a].add(b)
    elif t==2:
        relation[a]-= {b}
    else:
        if a in relation[b] and b in relation[a]:
            print('Yes')
        else:
            print('No')