import sys
input = sys.stdin.readline

def solver(s):
    arr = dict()
    for i in range(len(s)-1,-1,-1):
        if s[i] not in arr:
            arr[s[i]]=1
            last = i
        else:
            arr[s[i]]+=1

    print(s[last:])

for _ in range(int(input())):
    s = input().rstrip()

    solver(s)