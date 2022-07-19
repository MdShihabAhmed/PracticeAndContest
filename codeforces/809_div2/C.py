import sys

input = sys.stdin.readline

def solver(n, h):
    result = 0
    if n%2:
        for i in range(1,n-1,2):
            if h[i]<=h[i-1] or h[i]<=h[i+1]:
                result+=max(h[i-1],h[i+1])+1-h[i]
    else:
        temp = [0 for i in range(n)]
        for i in range(1,n-1):
            if h[i]<=h[i-1] or h[i]<=h[i+1]:
                temp[i]=max(h[i-1],h[i+1])+1-h[i]
        second = 0
        for i in range(2,n-1,2):
            second+=temp[i]
        result= second
        for i in range(1,n-1,2):
            result = min(result, second+temp[i]-temp[i+1])
            second = second+temp[i]-temp[i+1]
    
    print(result)
for _ in range(int(input())):
    n = int(input())
    h = list(map(int,input().split()))
    solver(n, h)