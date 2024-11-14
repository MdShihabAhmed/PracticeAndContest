import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int,input().split())
    if k==1:
        print(n)
        continue
    s = 0
    t = n
    while(t):
        t//=k
        s+=1
    result=0
    while(s>=0):
        if k**s<=n:
            temp = n//(k**s)
            result+=temp
            n -= (temp)*(k**s)
        else:
            s-=1
    print(result)