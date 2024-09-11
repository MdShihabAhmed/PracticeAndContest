import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = input().rstrip()

    letters = [0]*26
    for c in s:
        letters[ord(c)-97]+=1
    
    results = []

    j=0
    while(j<n):
        for i in range(26):
            if letters[i]:
                results.append(chr(i+97))
                letters[i]-=1
                j+=1
    
    print("".join(results))
        