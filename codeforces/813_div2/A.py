import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int,input().split())
    p = list(map(int,input().split()))
    result = 0
    for i in range(k):
        if p[i]>k:
            result+=1
    
    print(result)

