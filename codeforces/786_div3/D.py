import sys
    
input = sys.stdin.readline

def solver(n, a):
    if n==1:
        return 'YES'
    
    c = []
    if n%2:
        c.append(a[0])
        a.pop(0)
    for i in range(0,n-1,2):
        if a[i]>a[i+1]:
            c.append(a[i+1])
            c.append(a[i])
        else:
            c.append(a[i])
            c.append(a[i+1])

    for i in range(n-1):
        if c[i]>c[i+1]:
            return 'NO'

    return 'YES'

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    
    print(solver(n, a))