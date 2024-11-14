import sys

input = sys.stdin.readline
def query(i,j):
    print("?",i,j)
    sys.stdout.flush()
    r = int(input())
    if r==-1:
        exit(0)
    return r

for _ in range(int(input())):
    n = int(input())
    
    zero = [1]
    
    
    d = dict()
    d[str(1)] = []
    i = 0
    j = 2
    while(j<n):
        for k in range(i,len(zero)):
            if not query(zero[k],j):
                d[str(zero[k])].append(j)
                i = k
                break
        else:
            d[str(j)] = []
            zero.append(j)
        j+=1
    
    result = [0]*(n-1)
    for key,value in d.items():
        if not value:
            continue
        v = sorted(value)
        result[v[0]-1]=key
        for i in range(1,len(v)):
            result[v[i]-1]=v[i-1]
    
    print("!"," ".join(map(str,result)))
    sys.stdout.flush()

