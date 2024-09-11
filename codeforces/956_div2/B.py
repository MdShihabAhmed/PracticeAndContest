import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int,input().split())
    a = []
    for i in range(n):
        a.append(list(map(int,list(input().rstrip()))))
    b = []
    for i in range(n):
        b.append(list(map(int,list(input().rstrip()))))

    for i in range(n-1):
        for j in range(m-1):
            temp = (b[i][j]-a[i][j])
            if temp<0:
                temp+=3
            if temp==0:
                continue
            if temp==1:
                a[i][j]=(a[i][j]+1)%3
                a[i][j+1]=(a[i][j+1]+2)%3
                a[i+1][j]=(a[i+1][j]+2)%3
                a[i+1][j+1]=(a[i+1][j+1]+1)%3
            else:
                a[i][j]=(a[i][j]+2)%3
                a[i][j+1]=(a[i][j+1]+1)%3
                a[i+1][j]=(a[i+1][j]+1)%3
                a[i+1][j+1]=(a[i+1][j+1]+2)%3
        #     print(temp,end=" ")
        # print()
    flag = True 
    for i in range(n):
        for j in range(m):
            if a[i][j]!=b[i][j]:
                flag= False
                break
        if not flag:
            break
    if flag:
        print("YES")
    else:
        print("NO")