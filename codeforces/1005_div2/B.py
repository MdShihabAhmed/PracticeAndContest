import sys
from collections import defaultdict

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    d = defaultdict(int)
    for num in a:
        d[str(num)]+=1
    
    pre = [0]*(n)
    for i in range(n):
        if d[str(a[i])]==1:
            pre[i]=1

    result = 0
    l = 0
    r = 0
    temp= 0
    for i in range(n):
        if pre[i]==0:
            if result<temp:
                result = temp
                r = i-1
                l = r-temp+1

            temp = 0
        else:
            temp+=1
    if result<temp:
        r = n-1
        l = r-temp+1
        result = temp
    if result>0:
        print(l+1,r+1)
    else:
        print(0)