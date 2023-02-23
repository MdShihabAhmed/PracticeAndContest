import sys

input = sys.stdin.readline

for _ in range(int(input())):
    blank = input()
    n = int(input())
    R, G, B = 0, 0, 0

    for i in range(n):
        r, g, b = map(int,input().split())
        r+= min(G, B)
        g+= min(R, B)
        b+= min(R, G)
        R = r
        G = g
        B = b

    print("Case ",_+1,": ",min(R, G, B),sep="")
