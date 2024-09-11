import sys

input = sys.stdin.readline

def cal(l,r,c1,c2,pre):
    tempL = (((c1-1)+(l-1)%n+1)-1)%n+1
    tempR = (((c2-1)+(r-1)%n+1)-1)%n+1
    
    if tempL<=tempR:
        return (pre[tempR]-pre[tempL-1])
    else:
        return (pre[-1]- (pre[tempL-1]-pre[tempR]))

for _ in range(int(input())):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))

    pre = [0]
    for i in range(n):
        pre.append(pre[-1]+a[i])
    
    for i in range(k):
        l, r = map(int,input().split())
        result = 0
        
        c1 = (l+n-1)//n
        c2 = (r+n-1)//n
        
        result = pre[-1]*(max(0, (c2-c1-1)))
        

        if c2==c1:
            result+= cal(l,r,c1,c2,pre)
        else:
            result += cal(l,c1*n,c1,c1,pre)
            result += cal((c2-1)*n+1,r,c2,c2,pre)

        print(result)
