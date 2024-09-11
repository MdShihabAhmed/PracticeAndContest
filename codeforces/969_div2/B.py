import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))

    a.sort()
    result2 = []
    result = max(a)
    for i in range(m):
        c,l,r = input().split()
        l = int(l)
        r = int(r)
        if c=='+':
            if result<=r and result>=l:
                result+=1
        else:
            if result<=r and result>=l:
                result-=1
        result2.append(result)
    print(" ".join(map(str,result2)))
