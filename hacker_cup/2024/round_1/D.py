import sys

input = sys.stdin.readline
mod = 998244353
for test in range(int(input())):
    s, k = input().split()
    
    k = int(k)
    final = list(s)
    
    n = len(s)
    index = []
    
    for i in range(n):
        if final[i]=='?':
            index.append(i)
    
    kBin = bin(k)[2:]
    kBin = max(0,(len(index)-len(kBin)))*'1'+kBin
    print(s,k)
    print(index,len(index),kBin,len(kBin))
    
    if index:
        for i in range(len(kBin)-1,-1,-1):
            if kBin[i]=='1':
                final[index[i]]='2'

    # print(final)
    for i in range(n):
        if final[i]=='?':
            final[i]='1'
    
    d = "".join(final)
    
    L = len(d)
    dp = [0 for i in range(L+1)]
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2,L+1):
        dp[i] = 0
        
        c1 = int(d[i-2])
        c2 = int(d[i-1])
        
        if(c1==1 or (c1==2 and c2<=6)):
            dp[i] += dp[i-2]
            dp[i] %= mod
        if(c2!=0):
            dp[i] += dp[i-1]
            dp[i] %= mod

    print(f"Case #{test+1}: {d} {dp[L]%mod}")
        