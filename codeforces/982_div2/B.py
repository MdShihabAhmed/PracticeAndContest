import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    res = 0
    for i in range(n):
        temp = 0
        for j in range(i+1,n):
            if a[i]>=a[j]:
                temp+=1
        res = max(temp,res)
        
    
    print(n-(res+1))

    