import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    
    result = []
    for i in range(n):
        s = input().rstrip()
        for j in range(4):
            if s[j]=="#":
                result.append(j+1)
                break
    print(" ".join(map(str,result[::-1])))
    