import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    temp = max(a)
    result = 0
    temp1 = min(a)
    for i in range(1,n):
        result+=(temp-temp1)
    
    print(result)
    

    

    