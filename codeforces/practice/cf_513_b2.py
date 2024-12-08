import sys

input = sys.stdin.readline

for _ in range(1):
    n,k = map(int,input().split())
    tot = 2**(n-1)
    if tot<k:
        print(-1)
        continue

    result = []
    toAdd = 1
    half = 0
    per = {i for i in range(1,n+1)}
    while(True):
        tot//=2
        half += tot
        if k<=half:
            k -= (half-tot)
            half = 0
            result.append(toAdd)
            per.remove(toAdd)
        toAdd+=1
        if tot==0:
            break
    temp = list(per)
    temp.sort(reverse=True)
    if result:
        print(" ".join(map(str,result)),end=" ")
    print(" ".join(map(str,temp)))