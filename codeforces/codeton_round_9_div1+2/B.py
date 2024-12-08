import sys

input = sys.stdin.readline

for _ in range(int(input())):
    s = input().strip()
    if len(s)<2:
        print(-1)
        continue
    
    flag = False
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            print(s[i-1]+s[i])
            flag = True
            break
    if flag:
        continue
    
    if len(s)<3:
        print(-1)
        continue
    for i in range(2,len(s)):
        if s[i]!=s[i-1] and s[i-2]!=s[i-1] and s[i]!=s[i-2]:
            print(s[i-2]+s[i-1]+s[i])
            break
    else:
        print(-1)