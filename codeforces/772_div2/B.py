import sys

input = sys.stdin.readline

def solver(n,a):
    c=0
    if n<3:
        print(c)
        print(*a)
        return
    change = False

    for i in range(1,n-1):
        if change:
            a[i]=max(a[i-1], a[i+1])
            c+=1
            change = False

        if a[i]>a[i-1] and a[i]>a[i+1]:
            change = True
    if change:
        a[-1]=a[-2]
        c+=1
        change = False

    print(c)
    print(*a)



for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    # print(solver(n,a))
    solver(n,a)