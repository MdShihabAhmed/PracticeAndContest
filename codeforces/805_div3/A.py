import sys

input = sys.stdin.readline
arr = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]
def solver(m):
    for i in range(10):
        if arr[i]>m:
            return m-arr[i-1]
    return 0
for _ in range(int(input())):
    m = int(input())

    print(solver(m))