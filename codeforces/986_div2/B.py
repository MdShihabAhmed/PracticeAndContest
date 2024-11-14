import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, b,  c = map(int,input().split())
    if not b:
        if c<n-2:
            print(-1)
            continue
        result = n
        if c<n:
            result-=1
        
        print(result)
        continue
    

    result = 0
    cc = n
    r = 0
    if c<cc:
        cc -=(c)
        r+=1
        r+= ((cc-1)//b)
    # print(cc,n,r)
    result = (n-r)
        
    print(result)    

    