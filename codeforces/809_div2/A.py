import sys

input = sys.stdin.readline

def solver(n, m, a):
    result = ['B' for i in range(m)]
    for i in range(n):
        if m+1-a[i]>-1:
            if result[min(a[i],m+1-a[i])-1] == 'B':
                result[min(a[i],m+1-a[i])-1] = 'A'
            else:
                result[max(a[i],m+1-a[i])-1] = 'A'

    
    print(''.join([i for i in result]))

for _ in range(int(input())):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))

    solver(n, m, a)