import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    result = 0
    xL = xR = yL = yR = 0
    for i in range(n):
        x, y = map(int,input().split())
        if x<xL:
            xL = x
        elif x>xR:
            xR = x
        
        if y<yL:
            yL = y
        elif y>yR:
            yR = y
        
    
    print((abs(xL)+xR+abs(yL)+yR)*2)