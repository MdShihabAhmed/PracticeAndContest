import sys
from collections import defaultdict

input = sys.stdin.readline

for _ in range(int(input())):
    letters = list(input().split())
    n = int(input())
    tempDict = defaultdict(list)
    for i in range(n):
        s = input().rstrip()
        temp = []
        for c in s:
            temp.append(letters[ord(c)-65])
        temp = "".join(temp)
        tempDict[temp].append(s)
    
    for key, value in tempDict.items():
        if len(value)>1:
            print(f"Case #{_+1}: YES")
            break
    else:
        print(f"Case #{_+1}: NO")