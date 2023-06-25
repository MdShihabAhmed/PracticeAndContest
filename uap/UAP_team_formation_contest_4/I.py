import sys

input = sys.stdin.readline

for i in range(int(input()),3050):
    if i%4==2:
        print(i)
        break