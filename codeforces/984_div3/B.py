import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int,input().split())
    re = [0]*(k+1)
    for i in range(k):
        b,c = map(int,input().split())
        re[b]+=c
    
    re.sort()
    result = 0
    for i in range(k,max(0,k-n),-1):
        result+=re[i]
    
    print(result)