import sys

input = sys.stdin.readline


for _ in range(int(input())):
    n, m = map(int,input().split())
    carpet = []
    for i in range(n):
        line = list(input().rstrip())
        carpet.append(line)
    
    newCarpet = []
    forwardI = 0
    backwardI = n-1
    forwardJ = 0
    backwardJ = m-1
    result = 0
    check = ['1','5','4','3']
    while(forwardI<backwardI and forwardJ<backwardJ):
        temp = []
        for k in range(forwardJ,backwardJ+1):
            temp.append(carpet[forwardI][k])
        for k in range(forwardI+1,backwardI):
            temp.append(carpet[k][backwardJ])
        for k in range(backwardJ,forwardJ-1,-1):
            temp.append(carpet[backwardI][k])
        for k in range(backwardI-1,forwardI,-1):
            temp.append(carpet[k][forwardJ])
        
        for k in range(3):
            temp.append(temp[k])
        
        i = 0
        tempR = 0
        while(i<len(temp)-3):
            for k in range(4):
                if temp[k+i]!=check[k]:
                    i+=1
                    break
            else:
                i+=4
                result+=1

        
        forwardI +=1
        backwardI -=1
        forwardJ +=1
        backwardJ -=1
        
    print(result)      
