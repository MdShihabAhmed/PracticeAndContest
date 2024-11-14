import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, r = map(int,input().split())
    a = list(map(int,input().split()))
    s = sum(a)
    re = 0
    rr = 0
    for i in range(n):
        re+=(a[i]%2)
        rr+=(a[i]//2)
    
    r -= rr

    print(s-max((re-r),0)*2)

    

    