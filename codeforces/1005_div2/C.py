import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    temp = a[0]
    another = []
    for i in range(1,n):
        if a[i]>0:
            if temp>0:
                temp+=a[i]
            else:
                another.append(temp)
                temp = a[i]
        else:
            if temp<0:
                temp+=a[i]
            else:
                another.append(temp)
                temp = a[i]
    another.append(temp)
    
    suf = [0]*(len(another)+1)
    for i in range(len(another)):
        suf[i+1]=suf[i]
        if another[i]>0:
            suf[i+1]+=another[i]

    pre = [0]*(len(another)+1)
    for i in range(len(another)-1,-1,-1):
        pre[i]=pre[i+1]
        if another[i]<0:
            pre[i]+=abs(another[i])
    
    result = 0
    for i in range(len(another)+1):
        result = max(result,suf[i]+pre[i])
    
    print(result)