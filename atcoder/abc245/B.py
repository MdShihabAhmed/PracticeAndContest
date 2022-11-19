import sys
input = sys.stdin.readline

def solver(n,a):
    a = list(set(a))

    a.sort()
    for i in range(len(a)):
        if i!=a[i]:
            return i
    return len(a)
for _ in range(1):
    n = int(input())
    a = list(map(int,input().split()))
    print(solver(n,a))