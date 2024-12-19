import sys

input = sys.stdin.readline

def intt(s):
    return int(s,2)

for _ in range(int(input())):
    s = list(input().strip())
    n = len(s)
    start = -1
    end = -1
    total = intt("".join(s))

    for i in range(n):
        cur = 0
        if s[i]=='0':
            temp = n-i

            for j in range(n):
                if j>=i:
                    break
                if s[j]=="1":
                    here = intt("".join(s[j:j+temp]))

                    if total^here>=cur:
                        cur = total^here
                        start = j+1
                        end = j+temp
            break
    if start==-1:
        print(1,n,1,1)
    else:
        print(1,n,start,end)