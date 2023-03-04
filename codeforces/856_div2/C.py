import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))

    result = []
    l = 0
    for i in range(n):
        r = i+1 - l
        while(arr[l]<r and l<i):
            l += 1
            r -= 1
        result.append(r)
    print(" ".join([str(i) for i in result]))