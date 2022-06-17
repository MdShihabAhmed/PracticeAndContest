import sys

input = sys.stdin.readline

def solver(s):
    alllen = 0

    for c in s:
        alllen+=(ord(c)-96)
    if len(s)%2:
        if len(s)==1:
            print('Bob',alllen)
        else:
            alllen = max(alllen-(ord(s[-1])-96),alllen-(ord(s[0])-96)) - min((ord(s[-1])-96),(ord(s[0])-96))
            print('Alice',alllen)    
    else:
        print('Alice',alllen)
for _ in range(int(input())):
    s = input().rstrip()

    solver(s)