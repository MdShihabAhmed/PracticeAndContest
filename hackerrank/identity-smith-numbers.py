import sys
from math import sqrt
input = sys.stdin.readline

n = int(input())
m = n
divisors = []

i = 2
while(i<m+1):
    p = m
    if m%i==0:
        divisors.append(i)
        m//=i
    if m<=1:
        break
    if p==m:
        i+=1

sumOfDigits=0

while(n):
    sumOfDigits+=(n%10)
    n//=10

sumOfPrimes=0

for i in divisors:
    while(i):
        sumOfPrimes+=(i%10)
        i//=10

if sumOfDigits==sumOfPrimes:
    print(1)
else:
    print(0)