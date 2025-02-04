import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

for i in range(4):
    b = a[::]
    b[i],b[i+1]=b[i+1],b[i]
    if b==sorted(a):
        print("Yes")
        break
else:
    print("No")
