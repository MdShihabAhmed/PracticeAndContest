import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int,input().split())
    a = (n-k+1)

    if a%2==0:
        a+=1

    rr = (n-a+1)//2
    if n%2:
        rr+=1
    if (rr)%2:
        print("NO")
    else:
        print("YES")