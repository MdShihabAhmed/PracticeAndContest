import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    cnt = [0]*(n+1)
    for i in range(n):
        cnt[a[i]]+=1

    need = 0
    for i in range(n,0,-1):
        if need:
            if need+2<=cnt[i]:
                cnt[i]-=need+2
                need= 0
            else:
                need=need+2-cnt[i]
                cnt[i]=0
        need+=cnt[i]%2



    
    if need:
        print("No")
    else:
        print("Yes")
