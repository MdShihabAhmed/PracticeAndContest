import sys
from collections import Counter
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    s = sum(a)
    if s%n:
        print("NO")
        continue
    
    div = s//n
    pre = [0]
    for i in range(n):
        pre.append(div-a[i])
    
    # print(pre)
    for i in range(2,n+1):
        pre[i]+=pre[i-2]
    
    # print(pre)
    if pre[-1]==0 and pre[-2]==0:
        print("YES")
    else:
        print("NO")