import sys

input = sys.stdin.readline

def ask(l,r):
    print("?",l,r)
    sys.stdout.flush()
    ans = int(input())
    return ans

for _ in range(int(input())):
    n = int(input())
    if ask(1,2)==0:
        print("! IMPOSSIBLE")
        sys.stdout.flush()
        break
    result = ["0","1"]
    l=1
    r=3
    current = 1
    zeros = 1
    while(r<=n):
        if ask(l,r)-(current+zeros)==0:
            result.append("1")
            current+=zeros
        else:
            result.append("0")
            zeros+=1
            
        r+=1
    print("!","".join(result))
    sys.stdout.flush()