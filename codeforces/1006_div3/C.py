import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, x = map(int,input().split())
    s = bin(x)[2:]
    c = 0
    flag = True
    result = []
    orr = 0
    for i in range(n-1):
        temp = bin(c)[2:]
        if len(temp)>len(s):
            flag = False
            break
        for j in range(len(temp)-1,-1,-1):
            if temp[j]=='0':
                continue
            if s[len(s)-len(temp)+j]=="1":
                continue
            flag = False
            break
        if not flag:
            break
        orr = orr|c
        result.append(c)
        c+=1

    if orr|c==x:
        result.append(c)
    else:
        result.append(x)

    for i in range(c+1,n):
        result.append(x)
    
    print(" ".join(map(str,result)))