import sys
from collections import defaultdict

input = sys.stdin.readline
mod = 998244353

for _ in range(int(input())):
    n = int(input())
    tree = defaultdict(list)
    for i in range(n-1):
        x, y = map(int,input().split())
        tree[x].append(y)
    result = [0]*(n)
    result[0] = 1
