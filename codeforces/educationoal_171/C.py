import sys

input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    s = list(input().rstrip())
    
    i=n-1
    j=n-1
    zero = 0
    res = 0
    while(i>-1):
        zero = False
        while(i>-1):
            if s[i]=='0':
                zero = True
                break
            i-=1
        flag = False
        while(zero and j>i):
            if s[j]=='1':
                flag = True
                break
            j-=1
        if flag:
            s[j]=-1
            j-=1
        i-=1
        

    arr = []
    for i in range(n):
        if s[i]=='0':
            res+=(i+1)
        elif s[i]=='1':
            arr.append(i+1)
    
    nn = len(arr)
    nn = (nn+1)//2
    for i in range(nn):
        res+=arr[i]

    
    print(res)
        


    
    
