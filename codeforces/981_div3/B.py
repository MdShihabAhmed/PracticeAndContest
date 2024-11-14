import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
    
    result = 0
    
    for j in range(n):
        i = 0
        curr = float('inf')
        while(i<n and j<n):
            curr = min(curr,a[i][j])
            i+=1
            j+=1
        if curr<0:
            result += abs(curr)
    
    for i in range(1,n):
        j = 0
        curr = float('inf')
        while(i<n and j<n):
            curr = min(curr,a[i][j])
            i+=1
            j+=1
        if curr<0:
            result += abs(curr)
            
    print(result)