import sys

input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    if n==1:
        print(1)
        continue

    if n%2:
        res = float('inf')
        for i in range(0,n,2):
            j = 0
            temp = 0
            while(j+1<n):
                if i==j or i==j+1:
                    j+=1
                    continue
                temp = max(temp, a[j+1]-a[j])
                j+=2
            res = min(res,temp)
        
        print(res)

            

    else:
        k = 1
        for i in range(1,n,2):
            k = max(k,a[i]-a[i-1])
        print(k)