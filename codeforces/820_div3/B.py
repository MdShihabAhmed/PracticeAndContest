import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    t = input().rstrip()
    result = []
    i=n-1
    while(i>=0):
        if t[i]=='0':
            result.append(chr(96+int(t[i-2:i])))
            i-=2
        else:
            result.append(chr(96+int(t[i])))
        i-=1
    
    print(*result[::-1],sep='')

