import sys

input = sys.stdin.readline

def solver(n, a):
    for i in range(1,n):
        if a[i]%a[0]==0:
            continue
        return 'NO'
    return 'YES'

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    print(solver(n, a))