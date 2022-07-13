import sys
    
input = sys.stdin.readline

def solver(s, p):
    letters = [0 for i in range(26)]
    for c in s:
        letters[ord(c)-97]+=1

    total = 0
    for i in range(26):
        if letters[i]>0:
            total+=letters[i]*(i+1)
    if total<=p:
        print(s)
        return
    temp = 0
    i = 25
    while(i>=0):
        if letters[i]>0:
            temp+=(i+1)
            letters[i]-=1
        else:
            i-=1
        if total-temp<=p:
            break

    result = []
    for c in s:
        if letters[ord(c)-97]>0:
            result.append(c)
            letters[ord(c)-97]-=1
    
    print(''.join(c for c in result))
for _ in range(int(input())):
    s = input().rstrip()
    p = int(input())
    
    solver(s, p)