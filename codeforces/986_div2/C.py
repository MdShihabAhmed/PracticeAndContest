import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m, v = map(int,input().split())
    a = list(map(int,input().split()))
    pre = [0]
    for i in range(n):
        pre.append(pre[-1]+a[i])
    
    preMonster = [0]*(n+1)
    sufMonster = [0]*(n+1)
    temp = 0
    for i in range(n):
        temp+=a[i]
        preMonster[i+1]=preMonster[i]
        if temp>=v:
            preMonster[i+1]+=1
            temp = 0
    
    temp = 0
    for i in range(n-1,-1,-1):
        temp+=a[i]
        sufMonster[i]=sufMonster[i+1]
        if temp>=v:
            sufMonster[i]+=1
            temp = 0
    # print(pre)
    # print(preMonster)
    # print(sufMonster)
    if preMonster[-1]<m:
        print(-1)
        continue
    
    i = 0
    j = i+1
    result = 0
    while(i<=n and j<=n):
        while(j<=n and preMonster[i]+sufMonster[j]>=m):
            j+=1
        j-=1
        result = max(result,pre[j]-pre[i])
        i+=1
    print(result)