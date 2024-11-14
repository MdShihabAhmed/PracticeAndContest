from math import pi

x1,y1,x2,y2 = map(int,input().split())
n = int(input())
inter = 0


path = []
for i in range(n):
    x,y = map(int,input().split())
    if ((x>=x1 and x<=x2) or (x>=x2 and x<=x1)) and ((y>=y1 and y<=y2) or (y>=y2 and y<=y1)):
        inter+=1
        path.append([x,y])

if x1==x2 or y1==y2:
    result = (abs(x2-x1)+abs(y2-y1))*100-(inter*2*10)+(inter*pi*10)
    print(f"{result:.20f}")
    exit(0)
final = 0

if inter:
    path.sort()
    xx = path[0][0]
    yy = path[0][1]
    temp = 1
    final = 1
    for i in range(1,len(path)):
        if path[i][0]>xx and path[i][1]>yy:
            temp+=1
        else:
            final = max(temp,final)
            temp = 1
        xx = path[i][0]
        yy = path[i][1]
    final = max(temp,final)

result = (abs(x2-x1)+abs(y2-y1))*100-(final*2*10)+(final*(pi*5))

print(f"{result:.20f}")