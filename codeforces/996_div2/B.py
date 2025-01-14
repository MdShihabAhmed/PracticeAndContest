import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = [0]*n
    s = 0
    s1 = 0
    for i in range(n):
        if b[i]>a[i]:
            s+=(b[i]-a[i])
            c[i]=(b[i]-a[i])
            a[i]=b[i]
    
    for i in range(n):
        if (a[i]-(s-c[i]))<b[i]:
            print("NO")
            break
    else:
        print("YES")

    