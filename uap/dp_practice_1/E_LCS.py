import sys

input = sys.stdin.readline

def solver(s, t):
    dp = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    
    result = []
    i = len(s)
    j = len(t)
    while(i >= 0 and j >= 0):
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j-1]:
            j -= 1
        else:
            result.append(s[i-1])
            i -= 1
            j -= 1
    
    print(''.join(result[i] for i in range(len(result)-1,-1,-1)))


for i in range(1):
    s = input().rstrip()
    t = input().rstrip()
    solver(s, t)