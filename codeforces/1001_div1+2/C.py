import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    nn = n
    result = sum(a)

    for i in range(n):
        if len(a)<=1:
            break
        first = 0
        second = 0
        aa1 = []
        aa2 = []
        faa = 0
        saa = 0
        for i in range(1,nn):
            temp = (a[i]-a[i-1])
            first=temp 
            second=(-1*temp)
            aa1.append(first)
            aa2.append(second)
            faa+=first
            saa+=second

        
        if faa>=saa:
            a = aa1[::]
            result=max(result,faa)
        else:
            a = aa2[::-1]
            result=max(result,saa)
        nn-=1
    print(result)
