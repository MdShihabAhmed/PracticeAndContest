import sys

input = sys.stdin.readline

mod = 10**9+7

def calculate(p):
    result = 1
    y = 2

    while p>0:
        if p%2:
            result = ((result*y)%mod)
        y = (y*y)%mod
        p = p//2
    
    return result


n = int(input())
if n==0:
    print(1)
else:
    a = calculate(n-1) 
    b = (a%mod*2%mod)%mod
    b = (1%mod+b%mod)%mod

    print(((a%mod)*(b%mod))%mod)