import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))

    cnt = 0
    for i in range(1,n-k+2):
        cnt+=1
        if a[i]!=1:
            print("1")
            break
    else:
        if cnt>1:
            print("2")
        else:
            j = 1
            for i in range(1,n,2):
                if a[i]!=(j):
                    print(j)
                    break
                j+=1
            else:
                print(k//2+1)