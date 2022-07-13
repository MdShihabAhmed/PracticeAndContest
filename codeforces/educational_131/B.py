import sys
input = sys.stdin.readline

def solver(n):
    d = 2
    temp = [0 for i in range(n)]
    temp[0] = 1
    result = [i+1 for i in range(n)]
    t = 2
    i = 1
    while(i<n):
        if temp[t-1]:
            t+=1
            continue
        an = t
        while(an<=n):
            result[i]=an
            temp[an-1]=1
            an*=2
            i+=1
        t+=1

    print(d)
    print(' '.join([str(i) for i in result]))

    return 

for _ in range(int(input())):
    n = int(input())

    solver(n)