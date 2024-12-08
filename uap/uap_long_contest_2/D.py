import sys
from collections import defaultdict
from bisect import bisect_left

for _ in range(int(input())):
    z = input().strip()
    t = input().strip()
    index = defaultdict(list)

    for i in range(len(z)):
        index[z[i]].append(i)
    
    key = 0
    j = 0
    result = 0
    flag = True

    while(j<len(t)):
        ind = bisect_left(index[t[j]],key)

        if ind<len(index[t[j]]):
            key=index[t[j]][ind]+1
            j+=1
            continue
        if key==0:
            flag = False
            break
        result+=1
        key=0
    
    if key>0:
        result+=1

    if flag:
        print(result)
    else:
        print(-1)