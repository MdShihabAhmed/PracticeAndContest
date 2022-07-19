import sys

input = sys.stdin.readline

def solver(n, a):
    step = 0
    index = n
    for i in range(n):
        if a[i]>0:
            index = i
            break

    j = index+1

    while(j<n-1):
        if a[j]==0:
            a[index]-=1
            a[j]+=1
            step+=1
        j+=1
        if a[index]==0:
            index+=1
    for i in range(n-1):
        step+=a[i]
    return step
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    print(solver(n, a))