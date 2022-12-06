import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

a.sort()

newArr = []


for i in range(1, 2 * n):
    newArr.append(a[i] - a[i - 1])


first = 0
second = 0
temp = float("inf")
for i in range(2 * n - 1):
    for j in range(i + 1, 2 * n):
        k = 0
        temp2 = 0
        while k < 2 * n:
            if k == i or k == j:
                k += 1
                continue
            elif k + 1 == i or k + 1 == j:
                if k + 2 < 2 * n:
                    temp2 += abs(a[k] - a[k + 2])
                k += 2
                continue
            else:
                if k + 1 < 2 * n:
                    temp2 += abs(a[k] - a[k + 1])
                k += 2
        if temp2 < temp:
            temp = temp2

print(temp)
