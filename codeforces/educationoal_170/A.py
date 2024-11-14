import sys

input = sys.stdin.readline


for _ in range(int(input())):
    s = input().strip()
    t = input().strip()
    
    m = 0
    i = 0
    j = 0
    while(i<len(s) and j<len(t) and s[i]==t[j]):
        i+=1
        j+=1
        m+=1
    if m:
        print(len(s)+len(t)-m+1)
    else:
        print(len(s)+len(t))

    

