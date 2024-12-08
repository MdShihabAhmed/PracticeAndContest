import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    result = 1
    temp = 1
    while(temp<n):
        temp*=2
        temp+=2
        result+=1
    print(result)