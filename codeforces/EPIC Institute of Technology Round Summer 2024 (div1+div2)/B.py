import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    l = []
    for i in range(1,n):
        if a[i-1]>a[i]:
            l.append(a[i-1]-a[i])
            a[i]=a[i-1]
    l.sort()

    temp = 0
    result = 0
    for i in range(len(l)):
        result+=((len(l)-i)*(l[i]-temp)+(l[i]-temp))
        temp=l[i]

    print(result)
