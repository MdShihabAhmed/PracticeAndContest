import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    ind = []
    for i in range(n):
        ind.append([a[i],i])
    
    ind.sort()
    odd = False
    even = False
    temp = ind[-1][0]
    for i in range(n-1,-1,-1):
        if ind[i][0]==temp:
            if ind[i][1]%2:
                odd = True
            else:
                even = True
    if even:
        print(temp+(n+1)//2)
    else:
        print(temp+(n)//2)

