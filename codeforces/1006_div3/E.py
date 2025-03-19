import sys

input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    result = []
    x = 0
    y = 0
    while(k):
        n = (-1+(1+8*k)**0.5)//2
        n = int(n)
        k -= (n)*(n+1)//2
        for i in range(n+1):
            result.append((x,y))
            y+=1
        x+=1
    print(len(result))
    for v in result:
        print(*v)