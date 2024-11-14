import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    s = sum(a)
    mm = a[0]
    # print(a,k,s)
    mod=s%mm
    if mod:
        s+=(max(min(k,mm-mod),0))
        k-=(max(min(k,mm-mod),0))
    if s%mm:
        print(min(s%mm,n))
    else:
        print(min(s//mm+k//mm,n))
    
