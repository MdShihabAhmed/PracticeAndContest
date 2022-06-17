def solver(filename):
    input = open(filename+'.in', 'r').readline
    fout = open(filename+'.out', 'w')
    print = lambda x: fout.write(str(x)+'\n')

    n = int(input())

    none = [0, 1000]
    noneFlag = False
    total = [0, 0]
    result = []
    
    while(n):
        ramp, start, end = input().split()
        start = int(start)
        end = int(end)
        if ramp == 'none':
            if noneFlag:
                if start>none[0]:
                    none[0] = start
                if end<none[1]:
                    none[1] = end
            else:
                none[0] = start
                none[1] = end

            noneFlag = True
        else:
            if noneFlag:
                none[0] -= total[0]
                none[1] -= total[1]
                result.append(none)

            noneFlag = False

            if ramp == 'on':
                total[0] += start
                total[1] += end
            else:
                total[0] -= end
                total[1] -= start
        
        n -= 1

    print(str(result[0][0]) + ' ' + str(result[0][1]))
    print(str(result[0][0]+total[0]) + ' ' + str(result[0][1]+total[1]))

if __name__ == "__main__":
	solver('traffic')