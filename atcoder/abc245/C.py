import sys
input = sys.stdin.readline

def solver(n,k,a,b):
    av = bv = True
    for i in range(1,n):
        if av:
            if not(abs(a[i-1]-a[i])<=k or abs(a[i-1]-b[i])<=k):
                av = False
        
        if bv:
            if not(abs(b[i-1]-a[i])<=k or abs(b[i-1]-b[i])<=k):
                bv = False

        if not(av or  bv) :
            return "No"

    return "Yes"

for _ in range(1):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    print(solver(n,k,a,b))