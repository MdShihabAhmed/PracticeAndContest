import sys
input = sys.stdin.readline

def solver(n):
    pass
for _ in range(1):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    temp = [0 for i in range(n)]
    tempBack = [0 for i in range(n)]

    for i in range(1,n):
        if a[i-1]>a[i]:
            temp[i] = temp[i-1]+(a[i-1]-a[i])
        else:
            temp[i] = temp[i-1]
    for i in range(n-2,-1,-1):
        if a[i]<a[i+1]:
            tempBack[n-i-1] = tempBack[n-i-2]+(a[i+1]-a[i])
        else:
            tempBack[n-i-1] = tempBack[n-i-2]

    for i in range(m):
        s, t = map(int,input().split())
        if s<t:
            print(temp[t-1]-temp[s-1])
        else:
            print(tempBack[n-t]-tempBack[n-s])
