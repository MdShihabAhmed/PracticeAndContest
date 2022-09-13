import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m, Sx, Sy, d = map(int,input().split())
    if (abs(1-Sy)<=d or abs(n-Sx)<=d) and (abs(m-Sy)<=d or abs(1-Sx)<=d):
        print(-1)
        continue
    # if abs(n-Sx)+abs(m-Sy)<=d:
    #     print(-1)
    #     continue
    print(n-1+m-1)
