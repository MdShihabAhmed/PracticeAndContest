import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    for i in range(1,n//2):
        if a[i-1]==a[i] or a[n-i-1]==a[n-i]:
            a[i],a[n-i-1]=a[n-i-1],a[i]
    result = 0
    
    for i in range(1,n):
        if a[i-1]==a[i]:
            result+=1
    
    print(result)