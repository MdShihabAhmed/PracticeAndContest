import sys

input = sys.stdin.readline

for _ in range(int(input())):
    x,y,k = map(int,input().split())

    xx = (x//k)
    if x%k:
        xx+=1
    
    yy = (y//k)
    if y%k:
        yy+=1 
    result = 0
    if xx>yy:
        result+= yy*2 + (xx-yy)*2-1
    elif yy>xx:
        result+= xx*2 + (yy-xx)*2
    else:
        result+= xx*2

    print(result)
