input = open('billboard.in', 'r')
print = lambda x: open('billboard.out', 'w').write(str(x)+'\n')

def solver():
    pass

for _ in range(1):
    x1, y1, x2, y2 = map(int,input.readline().split())
    x3, y3, x4, y4 = map(int,input.readline().split())
    x = x2-x1
    y = y2-y1
    xT = False
    yT = False
    if x1>=x3 and x4>=x2:
        xT = True
        if y1>=y3 and y4<=y2:
            y-=(y4-y1)
        elif y1<y3 and y4>y2:
            y-=(y2-y3)
    if y1>=y3 and y4>=y2:
        yT = True
        if x1>=x3 and x4<=x2:
            x-=(x4-x1)
        elif x1<x3 and x4>x2:
            x-=(x2-x3)
    
    if xT and yT:
        x = 0
        y = 0
    print(x*y)