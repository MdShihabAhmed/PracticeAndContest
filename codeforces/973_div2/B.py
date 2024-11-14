import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    
    for i in range(n-2):
        a[n-2]-=a[i]
    
    print(a[-1]-a[-2])