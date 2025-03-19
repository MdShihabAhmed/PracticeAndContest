import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    result = [-1]*(n)

    temp = 1
    for i in range(n-2):
        if a[i]==1:
            if result[i]==result[i+1]:
                if result[i]==-1:
                    result[i]=temp 
                    result[i+1]=temp 
                    result[i+2]=temp 
                    temp+=1
                else:
                    result[i+2]=result[i]
            else:
                print("NO")
                break
        else:
            if result[i]==result[i+1]:
                if result[i]==-1:
                    pass
                else:
                    result[i+2]=temp
                    temp+=1
    else:
        print("YES")
