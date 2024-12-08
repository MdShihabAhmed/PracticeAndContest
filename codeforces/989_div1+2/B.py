import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n,m,k = map(int,input().split())
    s = input().strip()
    ze = 0
    i=0
    result = 0
    while(i<n):
        if s[i]=="0":
            ze+=1
        if s[i]=="1":
            ze=0
        if ze==m:
            result+=1
            i+=(k-1)
            ze=0
        i+=1
    
    print(result)

    