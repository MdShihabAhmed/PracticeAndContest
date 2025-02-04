import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        a.append([0]+list(map(int,input().split())))
        for j in range(1,n+1):
            a[i][j]+=a[i][j-1]
    
    result = [0]*(n+1)
    for i in range(n):
        for j in range(n):
            if a[i][n]-a[i][j]==(n-j):
                a[i][n]+=100000
                result[n-j]+=1

    for i in range(n+1):
        for j in range(1,i):
            if result[i] and (not result[j]):
                result[j]=1
                result[i]-=1

            
    
    for i in range(1,n+1):
        if not result[i]:
            print(i)
            break
    else:
        print(n)
            
    
        


    
