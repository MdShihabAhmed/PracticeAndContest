import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int,input().split())
    cX = 0
    cY = 0
    result = m*(4*n)

    x = 0
    y = 0
    for i in range(n):
        a,b = map(int,input().split())
        x+=a
        y+=b
        if i>0:
            result -= ((cX+m-x)*2+(cY+m-y)*2)
        cX=x
        cY=y
    
    print(result)
    