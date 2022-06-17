import sys
input = sys.stdin.readline

def solver(s):
    a = 0
    b = 0
    for c in s:
        if c=='a':
            if b==1:
                return 'NO'
            b=0
            a+=1
        else:
            if a==1:
                return 'NO'
            a=0
            b+=1
    if a==1 or b==1:
        return 'NO'
    return 'YES'

for _ in range(int(input())):
    s = input().rstrip()

    print(solver(s))