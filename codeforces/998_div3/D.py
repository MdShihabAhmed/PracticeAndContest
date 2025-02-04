import sys

input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    for i in range(1,n):
        temp = min(a[i],a[i-1])
        a[i]-=temp
        a[i-1]-=temp
        if a[i-1]>a[i]:
            print("NO")
            break
    else:
        print("YES")