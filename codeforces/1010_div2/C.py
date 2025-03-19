import sys

input = sys.stdin.readline

MOD = 10**9 + 7

for _ in range(int(input())):
    n = int(input())
    x = input().strip()
    
    xMod = 0
    for c in x:
        xMod = (xMod * 2 + (1 if c == '1' else 0)) % MOD
    
    if n == 1:
        print(0)
        continue
    
    pow_2 = pow(2, n-1, MOD)
    inv_pow_2 = pow(pow_2, MOD-2, MOD)
    
    term = (xMod * inv_pow_2) % MOD
    result = (n - 2 + term) % MOD
    print(result)