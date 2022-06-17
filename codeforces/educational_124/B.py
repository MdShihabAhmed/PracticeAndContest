import sys,math
input = sys.stdin.readline
a = [3**i for i in range(19)]

def solver(n):
    if n>19:
        print("NO")
        return
    
    print("YES")
    print(*a[:n])
   
for _ in range(int(input())):
    n = int(input())

    solver(n)