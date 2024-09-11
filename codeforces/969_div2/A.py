import sys

input = sys.stdin.readline

for _ in range(int(input())):
    l, r = map(int,input().split())
    if r-l+1<3:
        print(0)
    else:
        result = (r-l+1)//4
        if l%2:
            result+=((r-l+1)%4)//3
        print(result)
        
        
