def solver(n,k,a,b):
    for _ in range(n):
        for i in range(len(a)):
            if a[i]<=k:
                k+=b[i]
                b[i]=0

    return k


t = int(input())

for _ in range(t):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(solver(n,k,a,b))