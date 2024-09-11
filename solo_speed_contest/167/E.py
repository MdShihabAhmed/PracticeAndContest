import sys
from math import gcd
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    aa = []
    for i in enumerate(a):
        aa.append([i[1],i[0]])
    aa.sort()
    
    bb = []
    for i in enumerate(b):
        bb.append([i[1],i[0]])
    bb.sort()
    # print(aa)
    # print(bb)
    result = [set() for i in range(n)]
    temp1 = set()
    temp2 = set()
    for i in range(1,n):
        temp1.add(aa[i-1][1])
        result[aa[i][1]] = result[aa[i][1]].union(temp1)
        temp2.add(bb[i-1][1])
        result[bb[i][1]] = result[bb[i][1]].union(temp2)
    rr = []
    for i in range(n):
        rr.append(len(result[i]))
    rr.sort()
    # print(result)
    temp = rr[-1]
    r = 1
    for i in range(n-2,-1,-1):
        if temp == rr[i]:
            r+=1
    
    print(r)