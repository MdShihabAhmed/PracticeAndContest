import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    for i in range(1,n):
        temp = abs(a[i]-a[i-1])
        if not(temp == 5 or temp == 7):
            print("NO")
            break
    else:
        print("YES")