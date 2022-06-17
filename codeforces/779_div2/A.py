import sys

input = sys.stdin.readline

def solver(n,s):
    one = result = st = 0
    for i in range(n):
        if s[i]=='0':
            st = i
            break
    
    for i in range(st+1,n):
        if s[i]=='0':
            if one<2:
                result+=(2-one)
            one = 0
        else:
            one+=1
    return result
for _ in range(int(input())):
    n = int(input())
    s = input().rstrip()

    print(solver(n,s))