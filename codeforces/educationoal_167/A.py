import sys

input = sys.stdin.readline

for _ in range(int(input())):
    x,y = map(int,input().split())

    if x>0:
        if (x*-1)-1<=(x*-1)+y:
            print("YES")
        else:
            print("NO")
    else:
        if x-1<=(x)+y:
            print("YES")
        else:
            print("NO")

    

