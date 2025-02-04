import sys
from collections import defaultdict

input = sys.stdin.readline


for _ in range(int(input())):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    if sum(a)!=sum(b):
        print("NO")
        continue
    a.sort()
    b.sort()
    if n==m:
        if a==b:
            print("YES")
        else:
            print("NO")
        continue
    
    track = defaultdict(int)
    for num in a:
        track[str(num)]+=1
    
    flag = True
    while(b):
        num = b.pop()
        if track[str(num)]:
            track[str(num)]-=1
            continue
        if num==1:
            flag = False
            break
        first = num//2
        second = (num+1)//2
        b.append(first)
        b.append(second)
    
    for v in track.values():
        if v:
            flag = False
            break
    
    if flag:
        print("YES")
    else:
        print("NO")
