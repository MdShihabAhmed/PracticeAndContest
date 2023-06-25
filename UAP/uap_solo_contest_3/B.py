import sys

input = sys.stdin.readline

n, t1, t2, k = map(int,input().split())

result = []
for i in range(n):
    a, b = map(int,input().split())
    first = (a*t1)*((100-k)/100)+(b*t2)
    second = (b*t1)*((100-k)/100)+(a*t2)
    result.append((i+1, max(first, second)))

result.sort(key= lambda x: -x[1])

for i in range(n):
    print(f"{result[i][0]} {result[i][1]:.2f}")