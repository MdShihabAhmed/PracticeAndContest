import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

parent = defaultdict(int)
for i in range(n-1):
    parent[i+2] = arr[i]

result = []
temp = n
while(True):
    result.append(temp)
    if temp==1:
        break
    temp = parent[temp]

print(*result[::-1])

