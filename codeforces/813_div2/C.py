import sys

input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    tempArr = [0]*(n+1)
    rightMost = [0]*(n+1)

    for i in range(n):
        tempArr[i+1]=tempArr[i]
        if not rightMost[a[i]]:
            tempArr[i+1]+=1
        rightMost[a[i]]=i+1
    
    maxRight = 0
    flag = False
    for i in range(n-1,0,-1):
        if a[i]<a[i-1]:
            flag = True
            for j in range(i-1,-1,-1):
                if rightMost[a[j]] > maxRight:
                    maxRight = rightMost[a[j]]
        if flag:
            break
    print(tempArr[maxRight])

