import sys

input = sys.stdin.readline

def solver(n, l, r):
    result = []

    for i in range(1,n+1):
        j = l
        while(j<=r):
            if j%i==0:
                result.append(j)
                break
            j+=i-(j%i)
        else:
            break
    
    if len(result)==n:
        print('YES')
        print(' '.join([str(i) for i in result]))
    else:
        print('NO')
for _ in range(int(input())):
    n, l, r = map(int,input().split())

    solver(n, l, r)