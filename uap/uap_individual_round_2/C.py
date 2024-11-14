import sys

input = sys.stdin.readline

for _ in range(int(input())):
    k, n = map(int,input().split())
    # if n==1:
    #     print(f"{k} {1}/{1}")
    #     continue
    i = 0
    temp = n
    
    while(2**i<temp):
        temp-=(2**i)
        i+=1
    
    actual = 2**i
    have = temp
    p = 1
    q = 1
    while(i):
        i-=1
        actual//=2
        if (actual<have):
            have-=(actual)
            p = p+q
        else:
            q = p+q
        
    
    print(f"{k} {p}/{q}")