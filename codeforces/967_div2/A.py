import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    idx = [0]*(n+1)
    for i in range(n):
        idx[a[i]]+=1
    idx.sort()
    print(n-idx[-1])
