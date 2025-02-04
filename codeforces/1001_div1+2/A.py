import sys

input = sys.stdin.readline

for _ in range(int(input())):
    s = input().strip()
    result = 0
    for c in s:
        if c=="1":
            result+=1
    
    print(result)