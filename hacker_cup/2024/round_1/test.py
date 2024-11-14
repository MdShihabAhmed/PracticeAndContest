while(True):
    d = input()
    if(d[0]=='0'):
        break
    
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
        if(c2!=0):
            dp[i] += dp[i-1]
    
    print(dp[L])
