import sys
from collections import defaultdict

def check(colors,i,j,n,m,ch,t):
    if i<0 or i>=n or j<0 or j>=m:
        return t
    if colors[i][j]==ch:
        colors[i][j]=-1
        t+=1
        t = check(colors,i+1,j,n,m,ch,t)
        t = check(colors,i-1,j,n,m,ch,t)
        t = check(colors,i,j+1,n,m,ch,t)
        t = check(colors,i,j-1,n,m,ch,t)

    return t
        


input = sys.stdin.readline

for _ in range(int(input())):
    n,m = map(int,input().split())
    colors = []
    for i in range(n):
        temp = list(map(int,input().split()))
        colors.append(temp)
    
    d = defaultdict(int)
    for i in range(n):
        for j in range(m):
            if colors[i][j]<0:
                continue
            temp = colors[i][j]
            t = check(colors,i,j,n,m,temp,0)

            d[str(temp)] = min(2,max(t,d[str(temp)]))
    
    result= 0
    m = 0

    for k,v in d.items():
        m = max(m,v)
        result+=v
    
    print(result-m)