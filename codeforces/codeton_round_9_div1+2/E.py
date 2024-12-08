import sys

input = sys.stdin.readline

def ask(l,r):
    print("?",l,r)
    sys.stdout.flush()
    ans = int(input())
    return ans

for _ in range(int(input())):
    n = int(input())

    result = []
    l=1
    for i in range(2,n+1):
        ans = ask(1,i)
        if ans:
            result.append("1"*(i-ans-1))
            result.append("0"*(ans))
            result.append("1")
            l=(i-ans)
            r=i+1
            current = ans
            zeros = ans
            break
    else:
        print("! IMPOSSIBLE")
        sys.stdout.flush()
        continue
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