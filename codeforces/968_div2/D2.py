import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n,m = map(int,input().split())
    x = 0
    mex = []
    for i in range(n):
        temp = list(map(int,input().split()))
        temp2 = list(set(temp[1:]))
        temp2.sort()
        temp[0] = len(temp2)
        off = 0
        j = 0
        tempL = []
        while(j<temp[0]):
            if temp2[j]==j+off:
                j+=1
                continue
            x = max(x,j+off)
            tempL.append(j+off)
            off+=1
            if off>=2:
                break
        if off<1:
            tempL.append(j)
            tempL.append(j+1)
            x = max(x,j,j+1)
        elif off<2:
            tempL.append(j+off)
            x = max(x,j+off)
        mex.append(tempL)
    
    mex.sort()
    print(mex)
    mex2 = [0]*(10**6)
    mex3 = [0]*(10**6)
    tt = 0
    for i in range(len(mex)-1,-1,-1):
        
        mex2[mex[i][1]] = max(mex[i][1],mex2[mex[i][1]],mex2[mex[i][0]])
        mex2[mex[i][0]] = max(mex[i][1],mex2[mex[i][1]],mex2[mex[i][0]])
        mex3[mex[i][0]]=1 
        mex3[mex[i][1]]=1 
    
    
    x = 10**6
    first =0
    for i in range(10**6):
        if not mex2[i]:
            break
        x = i
        first+=mex2[i]
    first = sum(mex2)
    print(mex2[:15])
    print(mex3[:15])
    print(first)
    second = (max(m-x,0)*(2*(x+1)+max(m-x,0)-1))//2
    print(x,first,second,off)
    print(first+second)
    print()

    