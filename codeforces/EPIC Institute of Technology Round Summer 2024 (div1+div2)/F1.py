import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    for i in range(n):
        a[i] = [a[i],i+1]
    
    first = 0
    second = n-1
    result = 0
    while(second>-1):
        if not a[second][0] or a[second][1]<1:
            second-=1
        elif not first:
            second-=1
            first+=1
        else:
            if a[second][0]==a[second][1]:
                a[second][0]=0
                
                first-=1
                result+=1

            else:
                second -=1
                first+=1
    print(result)