import sys

input = sys.stdin.readline

d = []
sq =[]
s = 0
for i in range(5*(10**5)+10):
    s+=i
    d.append(s)
    temp = (s**0.5)
    if temp==int(temp):
        sq.append(i)


for _ in range(int(input())):
    n = int(input())
    s = n*(n+1)//2
    if n in sq:
        print(-1)
    else:
        result = [i for i in range(1,n+1)]
        for i in range(1,len(sq)):
            if sq[i]>n:
                break
            j = sq[i]-1
            result[j],result[j+1]=result[j+1],result[j]
        print(*result)
    