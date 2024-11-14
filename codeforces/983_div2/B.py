import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int,input().split())

    if n==1:
        print(1)
        print(1)
        continue
    if n==3:
        if k==2:
            print(1)
            print(1)
        else:
            print(-1)
        continue
    if k==1 or k==n:
        print(-1)
        continue
    if k%2==0:
        print(3)
        print(1,k,k+1)
        continue
    print(5)
    print(1,k-1,k,k+1,n)
