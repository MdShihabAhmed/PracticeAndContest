import sys

input = sys.stdin.readline

n, q = map(int,input().split())

arr = [[0]*(n+1) for i in range(n+1)]

for i in range(n):
    s = input().rstrip()
    for j in range(n):
        if s[j]=='*':
            arr[i+1][j+1]+=1

for i in range(1, n+1):
    for j in range(1, n+1):
        arr[i][j]+= arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1]

for i in range(q):
    y1, x1, y2, x2 = map(int,input().split())
    print(arr[y2][x2]-arr[y2][x1-1]-arr[y1-1][x2]+arr[y1-1][x1-1])