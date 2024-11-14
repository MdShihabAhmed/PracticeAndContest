import sys
from bisect import bisect
from collections import defaultdict

input = sys.stdin.readline

n, k = map(int,input().split())

l = []
dd = defaultdict(list)
for i in range(n):
    for j in list(map(int,input().split())):
        dd[j].append(i)

results = [0]*(n)
for key,value in dd.items():
    results[value[-1]] += 1


cnt = 0
for c in results:
    cnt+=c

r = 1/cnt

for i in range(n):
    results[i] = results[i]/cnt

for i in range(n):
    print(f"{results[i]:.8f}")
