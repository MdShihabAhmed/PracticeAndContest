import sys
from math import gcd
input = sys.stdin.readline


n,k = map(int,input().split())
a = list(map(int,input().split()))

av = [0]*(10)
for i in range(k):
    av[a[i]]+=1



result = n
i = 10
j = 1
while(n//j):
    d = (n%i)//j

    while(av[d]):

        n += (1)*j
        d = (n%i)//j
    i*=10
    j*=10
    


print(n)

