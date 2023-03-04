import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))

    for i in range(n):
        if arr[i]%2:
            arr[i]+=1

    for i in range(1,n):
        if arr[i]%arr[i-1]==0:
            arr[i]+=1
    
    print(" ".join([str(i) for i in arr]))