import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = list(input().split())
    
    temp = [s[0]]

    for i in range(1,n):
        if s[i]==temp[-1]:
            continue
        temp.append(s[i])
    
    if len(temp)==len(set(temp)):
        print(f"Case #{_+1}:"," ".join(temp))
    else:
        print(f"Case #{_+1}: IMPOSSIBLE")