import sys

input = sys.stdin.readline

def solver(a):
    newa = list(set(a))
    sizeofa = len(a)-len(newa)
    if sizeofa%2:
        return len(newa)-1
    return len(newa)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    print(solver(a))