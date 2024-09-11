import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a = input().rstrip()
    b = input().rstrip()
    result = len(a)
    r = 0
    for i in range(len(b)):
        cnt = 0
        j = i
        k = 0
        while(j<len(b) and k<len(a)):
            if a[k]==b[j]:
                cnt+=1
                j+=1
            k+=1
        r = max(r,cnt)
    print(result+(len(b)-r))