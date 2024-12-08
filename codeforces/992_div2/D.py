import sys
from collections import defaultdict

input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    tree = defaultdict(set)
    for i in range(n-1):
        u, v = input().split()
        tree[u].add(v)
        tree[v].add(u)
    
    print(tree)