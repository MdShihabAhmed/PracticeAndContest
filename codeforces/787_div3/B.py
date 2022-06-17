import sys

input = sys.stdin.readline

def solver(n, a):
    result = 0
    for i in range(n-2,-1,-1):
        while(a[i+1]<=a[i]):
            if a[i]==0:
                break
            result+=1
            a[i]=a[i]>>1
    flag = False
    for i in range(1,n):
        if a[i-1]>=a[i]:
            flag = True
            break
    if flag:
        return -1
    return result

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    print(solver(n, a))