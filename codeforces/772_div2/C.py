import sys

input = sys.stdin.readline

def solver(n,a):
    if a==sorted(a):
        print(0)
        return
    
    if a[-2]>a[-1]:
        print(-1)
        return
    if a[-1]<0:
        print(-1)
        return
    
    print(n-2)
    for i in range(n-2):
        print(i+1,n-1,n)



for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    # print(solver(n,a))
    solver(n,a)