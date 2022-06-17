def solver(filename):
    input = open(filename+'.in', 'r').readline
    fout = open(filename+'.out', 'w')
    print = lambda x: fout.write(str(x)+'\n')

    n = int(input())
    cow = []
    for i in range(n):
        cow.append(int(input()))
    
    result = float('inf')
    for i in range(n):
        summ = 0
        for j in range(n):
            summ+= cow[j]*j
        
        result = min(result,summ)
        cow.append(cow.pop(0))

    print(result)


if __name__ == "__main__":
	solver('cbarn')