def solver(l,r,k):
    if r==l:
        if r==1:
            return "NO"
        else:
            return "YES"
    
    n=(r-l)//2
    if (r%2!=0 or l%2!=0):
        n+=1

    if n<=k:
        return "YES"
    else:
        return "NO"

t = int(input())

for _ in range(t):
    l,r,k = map(int,input().split())
    print(solver(l,r,k))