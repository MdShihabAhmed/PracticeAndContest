import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))
    for i in range(1,n):
        arr[i]^=arr[i-1]
    
    print(arr)
