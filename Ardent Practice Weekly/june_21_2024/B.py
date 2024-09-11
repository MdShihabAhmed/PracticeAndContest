n = int(input())

re = 1

for i in range(2,int(n**(1/2))+1):
    if n%i==0:
        re = max(re,i)
        re = max(n//i,re)
print(n-re)