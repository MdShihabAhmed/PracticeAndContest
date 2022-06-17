import sys

n = int(sys.stdin.readline())

five = n//5

five += five//5

print(five)

result = 1

while(n!=1):
    if n%5:
        result*=n
    else:
        result*=(n//5)

    n-=1

print(result)
