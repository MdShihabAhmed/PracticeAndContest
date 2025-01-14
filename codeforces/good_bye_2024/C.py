import sys
from bisect import bisect_right
input = sys.stdin.readline

def cal(a,d,n):
    return int((n/2)*(2*a+(n-1)*d))
    return ((n*(2*a+(n-1)*d))//2)

for _ in range(int(input())):
    n, k = map(int,input().split())
    if k==1:
        print(n*(n+1)//2)
        continue
    nn = n
    result= 0

    last = 1
    inc = 0
    off = 0
    while(nn>=k):
        if nn%2:
            a = (nn+1)//2
            result += cal(a,nn,last)
            # print(result,result,inc,last)
            off+=(inc*(inc+1)//2)
            result += off 
            # result += (last*(last-1)//2)
            # print(result,result,inc,last)
            inc+=last
            last*=2
        nn//=2
    print(result)
        


