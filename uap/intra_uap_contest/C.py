import sys

input = sys.stdin.readline

while(True):
    n = int(input())
    if n==4:
        break
    t = 0
    while(True):
        i = 2
        prime = []
        t+=1
        while(i*i<=n):
            if n%i==0:
                while(n%i==0):
                    prime.append(i)
                    n//=i
            i+=1
        if n>1:
            prime.append(n)
        if len(prime)==1:
            print(prime[0],t)
            break
        n = sum(prime)