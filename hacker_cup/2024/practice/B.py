import sys

input = sys.stdin.readline

for test in range(int(input())):
    n, p = map(int,input().split())
    p/=100
    temp = p**((n-1)/n)
    result = (temp - p)*100

    print(f"Case #{test+1}: {result:.15f}")