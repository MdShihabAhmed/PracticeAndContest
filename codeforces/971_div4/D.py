import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    points = []
    y0 = [0]*n
    y1 = [0]*n
    
    for i in range(n):
        x, y = map(int,input().split())
        points.append([x,y])
        if y==0:
            y0[i]=1
        else:
            y1[i]=1

    i = 0
    j = 0
    result = 0
    while(i<len(y0) and j<len(y1)):
        if y0[i]==y1[j]:
            result+=(len(y0)-1+len(y1)-1)
        
        if i-1>=0 and i+1<len(y0) and y1[j]-y0[i-1]==1 and y0[i+1]-y1[j]==1:
            result+=1
        if j-1>=0 and j+1<len(y1) and y0[i]-y1[j-1]==1 and y1[j+1]-y0[i]==1:
            result+=1

        i+=1
        j+=1
        print(i,j)
    
        
    print(result)


    
    
