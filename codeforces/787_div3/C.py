import sys
    
input = sys.stdin.readline

def solver(s):
    if len(s)==1 or s[0]=='0' or s[-1]=='1':
        return 1
    result = 0
    for c in s:
        if c == '1':
            result = 1
        elif c== '?':
            result+=1
        else:
            result+=1
            break
    return result


    return result
for _ in range(int(input())):
    s = input().rstrip()
    
    print(solver(s))