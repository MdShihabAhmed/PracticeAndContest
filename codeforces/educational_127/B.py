import sys
input = sys.stdin.readline

def solver(n, a):
    if n==1:
        return 'YES'

    summ = 0
    for i in range(n-1):
        if a[i+1]-a[i]>=4:
            return 'NO'
        elif a[i+1]-a[i]==1:
            continue
        else:
            summ += a[i+1]-a[i]
        if summ>4:
            return 'NO'
        
    return 'YES'
   
for _ in range(int(input())):
    n = int(input())
    x = list(map(int,input().split()))

    print(solver(n, x))