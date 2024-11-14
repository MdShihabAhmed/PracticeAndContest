import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    total = sum(a)
    av = total//n

    have = max(0,a[0]-av)
    another = [min(a[0],av)]
    for i in range(1,n-1):
        if a[i]>=av:
            have+=a[i]-av
            another.append(av)
        else:
            t = min(av-a[i],have)
            another.append(a[i]+t)
            have-=t
    
    if a[n-1]<av and have:
        t = min(av-a[n-1],have)
        another.append(a[n-1]+t)
        have-=t
    else:
        another.append(a[n-1])

    print(another,have)
    
