import sys

input = sys.stdin.readline

def solver(a, n):
    if n<3:
        return 'YES'
    
    index = 0
    maxx = a[0]

    for i in range(n):
        if a[i]>maxx:
            maxx= a[i]
            index = i

    if sorted(a[:index])==a[:index] and sorted(a[index:],reverse=True)==a[index:]:
        return 'YES'
    
    return 'NO'


for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    print(solver(a, n))