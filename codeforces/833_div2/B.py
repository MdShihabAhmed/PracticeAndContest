import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = input()
    tt = len(set(s))
    result = 0
    for i in range(n):
        tem = 0
        temp = [0]*10
        t = 0
        for j in range(i,min(n, tt*tt)):
            if not temp[int(s[j])]:
                tem+=1
            temp[int(s[j])]+=1
            if temp[int(s[j])]>t:
                t = temp[int(s[j])]
            if tem>=t:
                result+=1
    
    print(result)