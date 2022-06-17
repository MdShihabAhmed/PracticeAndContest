import sys,math

input = sys.stdin.readline

def solver(n,m,x):
    w = [[val[0], val[1], val[2]] for val in sorted(x, key = lambda x: (x[2],x[1]))]
    w = w[:2*n]
    print(sum([i[2] for i in w]))
    w = [[val[0], val[1], val[2]] for val in sorted(w, key = lambda x: (x[1]))]
    for i in range(n):
        print(w[i][0],w[2*n-i-1][0])

for _ in range(int(input())):
    i = input()
    n, m = map(int,input().split())
    
    x = []
    w = []
    for i in range(m):
        xi, wi =map(int,input().split()) 
        x.append([i+1,xi,wi])

    solver(n,m,x)
    print()