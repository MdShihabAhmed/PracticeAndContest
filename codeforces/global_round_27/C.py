import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    l = [i for i in range(1,n+1)]
    if n&1:
        print(n)
        l[0],l[1]=l[1],l[0]
        print(" ".join(map(str,l)))
        continue
    
    k = 2**(len(bin(n))-2)-1
    s = len(bin(n))-2
    s-=1
    s = 2**s
    l = [i for i in range(1,s+1)]
    l[0],l[1]=l[1],l[0]
    l = [i for i in range(s+1,n+1)]+l
    print(k)
    print(" ".join(map(str,l)))