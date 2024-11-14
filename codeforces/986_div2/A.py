import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, a, b = map(int,input().split())
    s = input().strip()
    x = 0
    y = 0
    flag = False
    for j in range(100):
        for i in range(n):
            if s[i]=='N':
                y+=1
            elif s[i]=='S':
                y-=1
            elif s[i]=='E':
                x+=1
            elif s[i]=='W':
                x-=1
            if x==a and y==b:
                flag = True
                break
        if flag:
            break
    if flag:
        print("YES")
    else:
        print("NO")
        