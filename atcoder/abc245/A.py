import sys
input = sys.stdin.readline

def solver(a,b,c,d):
    if a<c:
        return "Takahashi"
    elif c<a:
        return "Aoki"
    else:
        if d<b:
            return "Aoki"
        else:
            return "Takahashi"

for _ in range(1):
    a,b,c,d= map(int,input().split())
    print(solver(a,b,c,d))