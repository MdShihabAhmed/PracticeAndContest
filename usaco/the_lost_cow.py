def solver(filename):
    input = open(filename+'.in', 'r').readline
    fout = open(filename+'.out', 'w')
    print = lambda x: fout.write(str(x)+'\n')

    x, y = map(int,input().split())
    move = 1
    result = 0
    xy = x
    while(True):
        xy=x+move
        if x<y and xy>=y:
            result+=(abs(move)*1.5-(xy-y))
            break
        elif x>y and xy<=y:
            result+=(abs(move)*1.5-(y-xy))
            break
        result+=(abs(move)*1.5)
        move*=-2
    print(int(result))

if __name__ == "__main__":
	solver('lostcow')