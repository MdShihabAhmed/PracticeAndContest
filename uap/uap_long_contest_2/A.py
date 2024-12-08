import sys

input = sys.stdin.readline

level = [0]

for i in range(1,1415+1):
    for j in range(i):
        level.append(i)

prefix = [0]
for i in range(1,10**6+406):
    prefix.append(prefix[-1]+i*i)


for _ in range(int(input())):
    n = int(input())
    result = 0
    minn = n 
    maxx = n
    while(True):

        result+=(prefix[maxx]-prefix[minn-1])
        if maxx==1:
            break
        # if level[maxx]==2:
        #     break
        N = (level[maxx]-1)
        S = (N*(N+1))//2
        numberMax = maxx-S
        numberMin = minn-S
        firstMin = numberMin-1
        secondMin = numberMin
        if numberMin==1:
            firstMin+=1
        if numberMin==N+1:
            secondMin-=1
        
        firstMax = numberMax-1
        secondMax = numberMax
        if numberMax==1:
            firstMax+=1
        if numberMax==N+1:
            secondMax-=1
        N-=1
        S2 = (N*(N+1))//2

        maxx = S2+max(firstMin,secondMin,firstMax,secondMax)
        minn = S2+min(firstMin,secondMin,firstMax,secondMax)

    print(result)
        
    