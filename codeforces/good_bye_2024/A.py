import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    c = 0
    i = 0
    while(i<n-1):
        te = min(a[i],a[i+1])
        te2 = max(a[i],a[i+1])
        if 2*te>te2:
            i+=2
            c = 1
            break 
        else:
            i+=1
    if c:
        print("YES")
    else:
        print("NO")