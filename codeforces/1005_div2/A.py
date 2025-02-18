import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    z = False
    o = False
    result = 0
    for i in range(n-1,-1,-1):
        if s[i]=='1':
            o = True
        if s[i]=='0':
            if o:
                result+=1
                if z:
                    result+=1
                z = False
                o = False
            z = True
    if o:
        result+=1
        if z:
            result+=1 
    
    print(result)
