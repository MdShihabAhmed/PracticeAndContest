import sys

input = sys.stdin.readline

MOD = 10**9+7

def base(n,p):
    temp = []
    while(n):
        temp.append(n%p)
        n//=p
    po = 0
    m = 0
    for i in range(len(temp)-1,-1,-1):
        m = (m+((pow(p,po,MOD))*temp[i])%MOD)%MOD
        po+=1
    return m


for _ in range(int(input())):
    n, k = map(int,input().split())
    result = 0
    for i in range(2,min(n,k)+1):
        result = (result+base(n,i))%MOD
    if n<k:
        result = (result+(n*(k-n))%MOD)%MOD
    print(result)
