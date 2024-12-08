import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int,input().split())
    divisors = [1]
    if n>1:
        divisors.append(n)
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            divisors.append(i)
            if i!=n//i:
                divisors.append(n//i)
    print(divisors)
    re = 0
    for d in divisors:
        dd = (n^d)
        if dd>=1 and dd<=m and dd!=n:
            re+=1
        dd = (n^dd)
        if dd>=1 and dd<=m and dd!=n:
            re+=1
    print(re)
    
    
    
