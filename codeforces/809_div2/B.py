import sys

input = sys.stdin.readline

def solver(n, c):
    result = [0 for i in range(n)]
    temp = [-1 for i in range(n)]
    for i in range(n):
        if temp[c[i]-1]<0:
            result[c[i]-1]+=1
        if temp[c[i]-1]>=0 and (i-temp[c[i]-1]-1)%2==0:
            result[c[i]-1]+=1
        temp[c[i]-1]=i

    
    print(' '.join([str(i) for i in result]))

for _ in range(int(input())):
    n = int(input())
    c = list(map(int,input().split()))

    solver(n, c)