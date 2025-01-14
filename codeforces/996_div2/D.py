import sys
from bisect import bisect_right

input = sys.stdin.readline

for _ in range(int(input())):
    n, k, l = map(int,input().split())
    sc = list(map(int,input().split()))
    sec = sc[0]
    pos = k
    i = 1
    while(pos<l):
        if i>=n:
            break
        if(pos>=sc[i]):
            if (pos-(sc[i]+sec)<k):
                pos =min(pos,sc[i]+sec)+k
        else:
            if (pos>=(sc[i]-sec)):
                pos =max(pos,sc[i]-sec)+k
            else:
                temp = (sc[i]-sec-pos)/2
                sec+=temp
                pos =max(pos,sc[i]-sec)+k
        i+=1

    if pos<l:
        sec += (l-pos)
    
    print(int(sec*2))
