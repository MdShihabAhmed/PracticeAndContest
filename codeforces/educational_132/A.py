import sys
input = sys.stdin.readline

def solver(s):
    pass

for _ in range(int(input())):
    x = int(input())
    a,b,c = (map(int,input().split()))
    unlocked = 0
    
    while(unlocked<4):
        if 1==x:
            unlocked+=1
            x=a
        elif 2==x:
            unlocked+=1
            x=b
        elif 3==x:
            unlocked+=1
            x=c
        else:
            break

    if unlocked==3:
        print('YES')
    else:
        print('NO')