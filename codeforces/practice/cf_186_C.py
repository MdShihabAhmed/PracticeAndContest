# Codeforces Round 118 (Div. 2) C. Plant
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

# solution equation is, sol = (4^n + 2^n)/2
# but n == 10^18, so we need to use fast exponentiation with modulus
# but modulus operator does not work on division same way as addition, subtraction and multiplication
# so we need to simplify 'sol' in a way that it has no division
# sol = (4^n + 2^n)/2
#     = (4^n + 2^n)*(2^-1)
#     = {(2*2)^n + 2^n}*(2^-1)
#     = {(2^n)*(2^n) + 2^n}*(2^-1)
#     = {2^n*(2^n + 1)}*(2^-1)
#     = {2^(n-1)*(2^n + 1)}

n = int(input())
if n==0:
    # as for n==0 the calculate function's 'p' goes to negative
    # so it does not work the way it supposed to.
    # rather than changing everything, as this is the only case where negative comes,
    # i just handled it separately :v
    print(1)
else:
    #2^(n-1)
    a = calculate(n-1) 
    #(2^n) -- simply multiplying a by 2
    b = (a%mod*2%mod)%mod
    #(2^n + 1)
    b = (1%mod+b%mod)%mod

    #{2^(n-1)*(2^n + 1)}
    print(((a%mod)*(b%mod))%mod)