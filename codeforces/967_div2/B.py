import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    if n&1:
        result = [0]*n
        result[n//2]=1
        temp = 1
        i = 1
        while(n//2-i>=0 and n//2+i<n):
            temp+=1
            result[n//2-i]=temp
            temp+=1
            result[n//2+i]=temp
            i+=1
        print(" ".join(map(str,result)))
    else:
        print(-1)