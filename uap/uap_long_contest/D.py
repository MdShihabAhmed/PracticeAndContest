import sys
from collections import Counter

for _ in range(int(input())):
    s = input().rstrip()
    cnt = Counter(s)
    result = 0
    for v in cnt.values():
        result = max(result,v)
    n = len(s)
    for i in range(10):
        for j in range(10):
            k = 0
            first = False
            current = 0
            while(k<n):
                if first and str(j)==s[k]:
                    current+=2
                    first = False
                    k+=1
                    continue
                if str(i)==s[k]:
                    first = True
                    k+=1
                    continue
                k+=1
            result= max(result, current)
    print(n-result)