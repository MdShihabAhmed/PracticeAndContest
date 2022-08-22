import sys

input = sys.stdin.readline

def solver(n, k, b, s):
    if k*b+(k-1)*n<s or k*b>s:
        print(-1)
        return
    result = [0]*n
    result[0]=k*b
    temp = s-(k*b)
    i = 0
    while(temp>0):
        result[i]+=(min(k-1,temp))
        i+=1
        temp-=(min(k-1,temp))
    
    print(*result)

for _ in range(int(input())):
    n, k, b, s = map(int,input().split())

    solver(n, k, b, s)