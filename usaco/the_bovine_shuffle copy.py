def solver(filename):
    input = open(filename+'.in', 'r').readline
    fout = open(filename+'.out', 'w')
    print = lambda x: fout.write(str(x)+'\n')

    n = int(input())
    a = list(map(int,input().split()))
    idNum = list(map(int,input().split()))
    array = [0]*n
    
    for i in range(3):
        for j in range(n):
            array[j]=idNum[a[j]-1]
        idNum = array[:]
    for i in idNum:
        print(i)

if __name__ == "__main__":
	solver('shuffle')