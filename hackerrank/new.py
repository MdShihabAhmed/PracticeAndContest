import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    result = 0
    for i in range(1,n+1):
        result^=i

    print(result)