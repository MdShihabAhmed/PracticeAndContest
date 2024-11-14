import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    if s[0]=='1' or s[-1]=='1':
        print('Yes')
        continue

    for i in range(1,n-1):
        if s[i]=='1' and(s[i-1]=='1' or s[i+1]=='1'):
            print('Yes')
            break
    else:
        print('No')

    