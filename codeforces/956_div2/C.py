import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    d = sum(a)
    tar = d//3
    if d%3:
        tar+=1
    
    aa = bb = cc = 0
    f = 0
    l = 0
    result = [[] for i in range(3)]
    print(result)
    flag = False
    for i in range(n):
        aa += a[i]
        bb += b[i]
        cc += c[i]
        if aa>=tar:
            result[0].append([f,i])
            flag = True
        if bb>=tar:
            result[1].append([f,i])
            flag = True 
        if cc>=tar:
            result[2].append([f,i])
            flag = True
        if flag:
            flag = False
            aa = bb = cc = 0
            f = i+1
        #     l+=1
        # if l>=3:
        #     break
    for i in range(3):
        if len(result[i])==0:
            print("YES")
    print(result)