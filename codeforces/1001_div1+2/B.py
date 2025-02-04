import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    if 1 in a:
        print("NO")
        continue
    if n==1:
        print("YES")
        continue

    for i in range(n):
        temp = a[i]-1
        if temp<(i-0)*2 or temp<(n-i-1)*2:
            print("NO")
            break
    else:
        print("YES")
    
    