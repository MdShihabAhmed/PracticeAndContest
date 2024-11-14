import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))

    rr = 0
    result = 0
    for i in range(n):
        if a[i]>=k:
            rr+=a[i]
        elif a[i]==0 and rr:
            rr-=1
            result+=1
    
    print(result)