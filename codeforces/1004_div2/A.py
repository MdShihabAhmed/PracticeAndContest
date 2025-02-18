import sys

input = sys.stdin.readline

for _ in range(int(input())):
    x, y = map(int,input().split())
    if x+1==y:
        print("Yes")
        continue
    temp = x
    flag = False
    while(temp>=9):
        temp-=9
        if temp+1==y:
            flag = True
            break
    
    if flag:
        print("Yes")
    else:
        print("No")