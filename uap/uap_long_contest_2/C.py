import sys 

input = sys.stdin.readline

n, k = map(int,input().split())
if n==1:
    divisors = [1]
else:
    divisors = [1,n]

i = 2
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        divisors.append(i)
        if i != n//i:
            divisors.append(n//i)


if len(divisors)<k:
    print(-1)
else:
    divisors.sort()
    print(divisors[k-1])


