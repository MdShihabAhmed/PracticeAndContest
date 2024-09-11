import sys

input = sys.stdin.readline

while(True):
    s = input().rstrip()
    if s=='0':
        break
    dp = [0]*(len(s)+1)
    dp[1] = 1
    if len(s)>=2:
        if (s[0]=='1' or s[0]=='2') and (int(s[1])<=6 and int(s[1])>0):
            dp[2] = 2
        else:
            dp[2] = 1

    for i in range(3,len(s)+1):
        if ((int(s[i-1])<=6 and int(s[i-1])>=1) and (s[i-2]=='1' or s[i-2]=='2')):
            dp[i] += (dp[i-1]+dp[i-2])
        else:
            dp[i] += dp[i-1]
    print(dp[-1])

