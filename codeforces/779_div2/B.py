import sys,math
input = sys.stdin.readline

def solver(n):
    if n%2:
        return 0
    m = 998244353
    return (math.factorial(n//2)*math.factorial(n//2))%m

for _ in range(int(input())):
    n = int(input())

    print(solver(n))