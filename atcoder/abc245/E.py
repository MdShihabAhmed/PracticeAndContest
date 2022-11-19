import sys
input = sys.stdin.readline

def solver(n,m,chocolate,box):
    chocolate.sort(key=lambda x: (x[0],x[1]))
    box.sort(key=lambda x: (x[0],x[1]))
    cnt = 0

    for i in range(n):
        for j in range(i,m):
            if chocolate[i][0]<=box[j][0] and chocolate[i][1]<=box[j][1]:
                box[j][0]=-1
                cnt+=1

    if cnt == n:
        return "Yes"
    return "No"
for _ in range(1):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    d = list(map(int,input().split()))

    chocolate = [[a[i],b[i]] for i in range(n)]
    box = [[c[i],d[i]] for i in range(m)]

    print(solver(n,m,chocolate,box))