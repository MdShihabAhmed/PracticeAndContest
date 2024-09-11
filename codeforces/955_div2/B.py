import sys

input = sys.stdin.readline

for _ in range(int(input())):
    x, y, k = map(int,input().split())
    # x+=1
    # k-=1
    # while(x%y==0):
    #     x//=y
    while(k>0 and x>1):
        temp = x%y
        x+= min(k,(y-temp))
        k-= min(k,(y-temp))
        while(x%y==0):
            x//=y
    
    x+=(k%(y-1))
    print(x)