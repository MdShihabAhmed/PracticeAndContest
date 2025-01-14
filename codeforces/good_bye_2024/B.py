import sys
from collections import defaultdict
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    ss = [0]*(2*n+1)
    result = ["1" for i in range(n)]
    unique = defaultdict(list)
    check = []
    for i in range(n):
        l,r = map(int,input().split())
        if l==r:
            ss[l]=1
            unique[str(l)].append(i)
        else:
            check.append([l,r,i])
    
    for i in range(2*n):
        ss[i+1]+=ss[i]
    
    for key,value in unique.items():
        if len(value)>1:
            for i in value:
                result[int(i)]="0"
    
    for v in check:

        if v[1]-v[0]+1<=ss[v[1]]-ss[v[0]-1]:
            result[v[2]]="0"
    
    print("".join(result))
